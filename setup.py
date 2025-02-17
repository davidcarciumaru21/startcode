#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread
from errors import *
import math

# ************ ROBOT ************

class Robot:
    """
    Clasa care definește robotul și toate metodele sale.
    """

    def __init__(self, WHEELDIAMETER: float, AXLETRACK: float) -> None:
        """
        Inițializează robotul cu dimensiunile roților și ecartamentul.
        """
        self.WHEELDIAMETER: float = WHEELDIAMETER  # ! Constanta. Nu o modifica!
        self.AXLETRACK: float = AXLETRACK  # ! Constanta. Nu o modifica!

        # Inițializarea motoarelor
        self.st: object = self.initMotor(Port.A, "Left motor", Direction.CLOCKWISE)
        self.dr: object = self.initMotor(Port.D, "Right motor", Direction.CLOCKWISE)
        self.bratSt: object = self.initMotor(Port.C, "Left arm motor")
        self.bratDr: object = self.initMotor(Port.B, "Right arm motor")

        # Inițializarea senzorilor
        self.touch: object = self.initSensor(TouchSensor, Port.S4, "Touch sensor")
        self.gyro: object = self.initSensor(GyroSensor, Port.S1, "Gyro sensor")
        self.colourDr: object = self.initSensor(ColorSensor, Port.S2, "Colour sensor right")
        self.colourSt: object = self.initSensor(ColorSensor, Port.S3, "Colour sensor left")

        # Inițializarea bazei de mișcare
        self.d: object = DriveBase(
            self.st, self.dr, self.WHEELDIAMETER, self.AXLETRACK)

        # Blocări pentru thread-uri
        self.lock0: object = _thread.allocate_lock()
        self.lock1: object = _thread.allocate_lock()
        self.lock2: object = _thread.allocate_lock()
        self.lock3: object = _thread.allocate_lock()
        self.threadStopFlag: bool = False

        # Lista motoarelor
        self.motorList: list = [self.st, self.dr, self.bratSt, self.bratDr]

    # ************ INITIALIZATION ************
    def initMotor(self, port: Port, name: str, direction=Direction.CLOCKWISE) -> Motor:
        """
        Inițializează un motor și gestionează erorile.
        """
        try:
            return Motor(port, direction)
        except Exception:
            raise UnableToFindMotor(name)

    def initSensor(self, sensorClass: object, port: Port, name: str) -> object:
        """
        Inițializează un senzor și gestionează erorile.
        """
        try:
            return sensorClass(port)
        except Exception:
            raise UnableToFindSensor(name)

    # ************ DRIVETRAIN AND MOTOR CONTROL ************
    def stopRobot(self) -> None:
        """
        Oprește toate motoarele.
        """
        for motor in self.motorList:
            motor.stop()

    def holdRobot(self) -> None:
        """
        Menține toate motoarele în poziție.
        """
        for motor in self.motorList:
            motor.hold()

    def stopDriveTrain(self) -> None:
        """
        Opreste toate motoarele de la sasiu
        """
        self.dr.stop()
        self.st.stop()

    def driveToTarget(self, target: int, power: int) -> None:
        """
        Mergi până la un anumit target, rulând motoarele simultan.
        """
        self.dr.run_angle(power, target, wait=False)  # Nu așteaptă finalizarea mișcării
        self.st.run_angle(power, target, wait=True)   # Așteaptă finalizarea mișcării

    def drive(self, powerDr: int, powerSt: int) -> None:
        """
        Rulează motoarele continuu la viteze diferite.
        """
        self.dr.run(powerDr)
        self.st.run(powerSt)
    
    def runDrUntilStalled(self, powerDr):
        self.dr.run_until_stalled(powerDr)

    def runStUntilStalled(self, powerSt):
        self.st.run_until_stalled(powerSt)

    def driveUntilStalled(self, powerDr: int, powerSt: int) -> None:
        _thread.start_new_thread(self.runDrUntilStalled, (powerDr,)) 
        _thread.start_new_thread(self.runStUntilStalled, (powerSt,)) 

    def moveByCm(self, distance: int, speed: int, motor: object, diameter = self.WHEELDIAMETER: float) -> None:
        """
        Deplasează un motor pe o distanță specificată, calculând numărul necesar de grade pentru motor.

        distance: Distanța dorită în centimetri.
        speed: Viteza motoarelor.
        """

        # Calculăm câte grade trebuie să rotească motoarele
        degrees: float = (distance * 360) / (math.pi * self.WHEELDIAMETER)

        # Pornim motorul pentru a se roti numărul calculat de grade
        self.motor.run_angle(speed, degrees, Stop.BRAKE)

    def driveByCm(self, distance: int, speed: int) -> None:
        """
        Deplasează robotul pe o distanță specificată, calculând numărul necesar de grade pentru motoare.

        distance: Distanța dorită în centimetri.
        speed: Viteza motoarelor.
        """

        # Calculăm câte grade trebuie să rotească motoarele
        degrees: float = (distance * 360) / (math.pi * self.WHEELDIAMETER)

        # Pornim motoarele pentru a se roti numărul calculat de grade
        self.st.run_angle(speed, degrees, Stop.BRAKE, wait=False)
        self.dr.run_angle(speed, degrees, Stop.BRAKE, wait=True)

    # ************ THREAD CONTROL ************
    def startThreads(self) -> None:
        """
        Permite rularea thread-urilor.
        """
        self.threadStopFlag = False

    def stopThreads(self) -> None:
        """
        Oprește toate thread-urile.
        """
        self.threadStopFlag = True

    # ************ MOVE WITH THREADS ************
    def runThread(self, function: callable, args: tuple) -> None:
        """
        Pornește un nou thread dacă acestea nu sunt oprite.
        """
        if not self.threadStopFlag:
            _thread.start_new_thread(function, args)

    def straightThreaded(self, distance: int, lock: object) -> None:
        """
        Deplasează robotul drept într-un mod asincron.
        """
        with lock:
            self.d.straight(distance)

    def runMotorByTimeThreaded(self, speed: int, duration: int, motor: Motor, lock: object) -> None:
        """
        Rulează un motor pentru o anumită perioadă în mod asincron.
        """
        with lock:
            motor.run_time(speed, duration)

    def runMotorByAngleThreaded(self, speed: int, angle: int, motor: Motor, lock: object) -> None:
        """
        Rulează un motor la un unghi specific într-un mod asincron.
        """
        with lock:
            motor.run_angle(speed, angle)

    # ************ METHODS WITH GYRO ************
    def gotoGyroPID(self, Kp: float, Ki: float, Kd: float, targetAngle: int, tolerance: int = 1) -> None:
        """
        Utilizează senzorul giroscopic pentru a roti robotul la un unghi țintă folosind un regulator PID.
        
        Argumente:
        Kp : float - coeficientul proporțional (folosit pentru a ajusta viteza în funcție de eroare)
        Ki : float - coeficientul integrator (compensează erorile acumulate pe termen lung)
        Kd : float - coeficientul derivativ (ajută la reducerea oscilațiilor și îmbunătățirea răspunsului)
        targetAngle : int - unghiul țintă la care trebuie să ajungă robotul
        tolerance : int - toleranța acceptabilă pentru a considera că robotul a ajuns la unghiul dorit (implicit 1)
        """

        # Inițializează eroarea anterioară (pentru calculul derivativ)
        previousError: float = 0
        # Inițializează valoarea integralului (pentru compensarea erorilor acumulate)
        integral: float = 0

        while True: 
            currentAngle: float = self.gyro.angle()

            # Calculul erorii (diferența între unghiul țintă și cel curent)
            error: float = targetAngle - currentAngle
            # Actualizează valoarea integralului (integrarea erorii în timp)
            integral += error * 0.01
            # Calculul derivativului (schimbarea erorii în timp)
            derivative: float = (error - previousError) / 0.01
            # Calculul ieșirii PID (proporțional + integrativ + derivativ)
            output: float = Kp * error + Ki * integral + Kd * derivative

            self.drive(-output, output)

            previousError: float = error

            # Verifică dacă eroarea este suficient de mică pentru a considera că robotul a ajuns aproape de țintă
            if abs(error) <= tolerance:
                break  
    
    def gotoGyro(self, targetAngle: int, power: int, tolerance: int = 1) -> None:

        """
        Această funcție ajustează direcția robotului pentru a ajunge la unghiul țintă specificat,
        ținând cont de toleranța dată.
        
        Parametri:
        - targetAngle: unghiul țintă la care robotul trebuie să ajungă (în grade).
        - speed1: viteza motorului stâng.
        - speed2: viteza motorului drept.
        - tolerance: toleranța (în grade) față de unghiul țintă la care considerăm că am ajuns (implicit 1 grad).
        """

        # Continuăm să ajustăm unghiul robotului până când ajungem la unghiul țintă
        while True:
            currentAngle: float = self.gyro.angle()  # Obținem unghiul curent al robotului de la giroscop

            # Verificăm dacă unghiul țintă a fost atins (cu o toleranță de 1 grad)
            if abs(currentAngle - targetAngle) < tolerance:
                break  # Ieșim din buclă când suntem suficient de aproape de unghiul țintă

            if currentAngle < 0:
                # Dacă unghiul curent este negativ, facem robotul să vireze într-o direcție
                self.drive(-power, power)
            else:
                # Dacă unghiul curent este pozitiv, facem robotul să vireze în direcția opusă
                self.drive(power, -power)

    def straightWithGyro(self, distance: int, power: int) -> None:
        """
        Merge o distanța pe o linie dreaptă, corectând direcția cu ajutorul giroscopului.
        
        Parametri:
        - distance: distanța pe care robotul trebuie să o parcurgă (în unități corespunzătoare).
        - power: puterea (viteza) motoarelor pentru deplasare.
        """
        
        previousAngle: float = self.gyro.angle() 
        previousDistanceTravelled: float = self.dr.angle() 
        
        while True:
            distanceTravelled: float = self.dr.angle() - previousDistanceTravelled
            
            if abs(distanceTravelled) >= distance:
                break

            correction: float = self.gyro.angle() - previousAngle
            self.drive(power - correction, power + correction)
            
            previousAngle: float = self.gyro.angle()
            previousDistanceTravelled: float = self.dr.angle()  

        self.stopRobot()

        # ************ METHODS WITH COLOUR SENSORS ************

    def followLine(self, colour: object, sensor: object, power: int, target: int) -> None:

        """
        Merge pe o linie, urmarind o anumita culoare de pe aceasta folosindu-se de sensorul de culoare
            
        Parametri:
        - colour: culoare pe care o cauta
        - sensor: senzorul de culoare pe care vrem sa-l folosim
        - power: viteza cu care sa mearga robotul
        - target: pozitia la care vrem sa ajunga robotul
        """

        initial: float = self.dr.angle()  # Salvează unghiul inițial al motorului (poziția de început)
        
        while True:
            # Calculează distanța parcursă până acum
            distanceTravelled: float = abs(self.dr.angle() - initial)
            detectedColor: object = sensor.color()  # Obține culoarea detectată de senzor
                
            # Oprește robotul dacă s-a parcurs distanța dorită
            if distanceTravelled >= target and detectedColor == colour:
                self.stop()  # Oprește robotul după ce s-a atins distanța țintă
                break
                
            detectedColor: object = sensor.color()  # Obține culoarea detectată de senzor
                
            if detectedColor == colour:
                # Dacă culoarea corectă este detectată, robotul merge înainte
                self.drive(power, power)
            else:
                # Dacă culoarea nu este detectată, robotul caută linia
                self.drive(0, power)  # Se rotește spre dreapta
                    
                # Verifică din nou culoarea după rotație
                detectedColor: object = sensor.color()
                if detectedColor != colour:
                    self.drive(power, 0)  # Se rotește spre stânga pentru a continua căutarea liniei

    def allignToLine(self, colour: object, power: int) -> None:
        """ 
        Aliniază robotul la o linie detectată de senzori.
        
        Parametri:
        - colour: culoarea liniei la care robotul trebuie să se alinieze
        - power: viteza de deplasare a roților 
        """

        # Robotul se deplasează înainte până când unul dintre senzori detectează linia
        while self.colourDr.color() != colour and self.colourSt.color() != colour:
            self.drive(power, power)

        # Oprește robotul pentru a face ajustări
        self.stop()
        
        # Verifică dacă senzorul drept a detectat linia primul
        if self.colourDr.color() == colour:
            # Mișcă doar roata stângă până când și senzorul stâng detectează linia
            while self.colourSt.color() != colour:
                self.drive(0, power)
        
        # Verifică dacă senzorul stâng a detectat linia primul
        elif self.colourSt.color() == colour:
            # Mișcă doar roata dreaptă până când și senzorul drept detectează linia
            while self.colourDr.color() != colour:
                self.drive(power, 0)
        
        # Oprește robotul după ce ambii senzori detectează linia
        self.stopDriveTrain()

    def followLinePID(self, sensor: object, color: object, fallBack: int, distance: int, power: int, Kp: float, Ki: float, Kd: float) -> None:
        initialDistance: float = self.dr.angle()  # Salvează distanța inițială
        lastError: float = 0
        integral: float = 0

        while abs(self.dr.angle() - initialDistance) < distance:
            if sensor.color() == color:
                referenceValue: float = sensor.reflection()  # Folosește valoarea reală când detectează culoarea
            else:
                referenceValue: float = fallBack  # Folosește valoarea fallback când senzorul nu detectează culoarea

            error: float = referenceValue - sensor.reflection()
            integral += error
            derivative: float = error - lastError
            correction: float = Kp * error + Ki * integral + Kd * derivative
            lastError: float = error

            self.drive(power + correction, power - correction)

        self.stopDriveTrain()

    # ************ MIXED METHODS ************
    def alignToLineMixed(self, angle: int, colour: object, power: int) -> None:
        """
        Funcție pentru alinierea robotului la o linie folosind doi senzori de culoare.
        
        - angle: unghiul inițial față de care se va face corectarea
        - colour: culoarea liniei la care ne aliniem
        - power: viteza motoarelor în timpul alinierei
        """

        angleIncrementer: int = 0 

        while self.sensorDr.color() != colour and self.sensorSt.color() != colour:
            self.drive(power, power)  # Ambele motoare merg înainte

        self.stopDriveTrain()  # Oprire pentru a evita depășirea liniei

        if self.sensorDr.color() == colour and self.sensorSt.color() != colour:
            # Dacă doar senzorul din dreapta a detectat linia, rotim ușor robotul spre stânga
            while self.sensorSt.color() != colour:
                self.gotoGyro(angle + angleIncrementer, 300, 0)
                angleIncrementer += 1  # Creștem ușor unghiul pentru o aliniere fină

        elif self.sensorSt.color() == colour and self.sensorDr.color() != colour:
            while self.sensorDr.color() != colour:
                self.gotoGyro(angle - angleIncrementer, 300, 0)
                angleIncrementer += 1  # Creștem ușor unghiul pentru o aliniere fină

        # Oprire finală după aliniere
        self.stopDriveTrain()