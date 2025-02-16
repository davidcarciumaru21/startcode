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

# ************ ROBOT ************

class Robot:
    """
    Clasa care definește robotul și toate metodele sale.
    """

    def __init__(self, WHEELDIAMETER: float, AXLETRACK: float) -> None:
        """
        Inițializează robotul cu dimensiunile roților și ecartamentul.
        """
        self.WHEELDIAMETER = WHEELDIAMETER  # ! Constanta. Nu o modifica!
        self.AXLETRACK = AXLETRACK  # ! Constanta. Nu o modifica!

        # Inițializarea motoarelor
        self.st = self.initMotor(Port.A, "Left motor", Direction.CLOCKWISE)
        self.dr = self.initMotor(Port.D, "Right motor", Direction.CLOCKWISE)
        self.bratSt = self.initMotor(Port.C, "Left arm motor")
        self.bratDr = self.initMotor(Port.B, "Right arm motor")

        # Inițializarea senzorilor
        self.touch = self.initSensor(TouchSensor, Port.S4, "Touch sensor")
        self.gyro = self.initSensor(GyroSensor, Port.S1, "Gyro sensor")

        # Inițializarea bazei de mișcare
        self.d = DriveBase(
            self.st, self.dr, self.WHEELDIAMETER, self.AXLETRACK)

        # Blocări pentru thread-uri
        self.lock0 = _thread.allocate_lock()
        self.lock1 = _thread.allocate_lock()
        self.lock2 = _thread.allocate_lock()
        self.lock3 = _thread.allocate_lock()
        self.threadStopFlag = False

        # Lista motoarelor
        self.motorList = [self.st, self.dr, self.bratSt, self.bratDr]

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

    # ************ DRIVETRAIN CONTROL ************
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

    def stopDriveTrain(self) -> None:
        """
        Menține motoarele sasiului în poziție.
        """
        self.dr.hold()
        self.st.hold()

    def driveToTarget(self, target: int, power: int) -> None:
        """
        Mergi pana la un anumit target
        """

        # Pornim ambele motoare simultan spre ținta dorită
        self.dr.run_angle(power, target)
        self.st.run_angle(power, target)

    def drive(self, powerDr: int, powerSt: int) -> None:
        self.dr.run(powerDr)
        self.st.run(powerSt)
    
    def runDrUntilStalled(self, powerDr):
        self.dr.run_until_stalled(powerDr)

    def runStUntilStalled(self, powerSt):
        self.st.run_until_stalled(powerSt)

    def driveUntilStalled(self, powerDr: int, powerSt: int) -> None:
        _thread.start_new_thread(self.runDrUntilStalled, (powerDr,)) 
        _thread.start_new_thread(self.runStUntilStalled, (powerSt,)) 

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
        previousError = 0
        # Inițializează valoarea integralului (pentru compensarea erorilor acumulate)
        integral = 0

        while True: 
            currentAngle = self.gyro.angle()

            # Calculul erorii (diferența între unghiul țintă și cel curent)
            error = targetAngle - currentAngle
            # Actualizează valoarea integralului (integrarea erorii în timp)
            integral += error * 0.01
            # Calculul derivativului (schimbarea erorii în timp)
            derivative = (error - previousError) / 0.01
            # Calculul ieșirii PID (proporțional + integrativ + derivativ)
            output = Kp * error + Ki * integral + Kd * derivative

            self.drive(-output, output)

            previousError = error

            # Verifică dacă eroarea este suficient de mică pentru a considera că robotul a ajuns aproape de țintă
            if abs(error) <= tolerance:
                break  
    
    def gotoGyro(self, targetAngle: int, speed1: int, speed2: int, tolerance: int = 1) -> None:

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
            currentAngle = self.gyro.angle()  # Obținem unghiul curent al robotului de la giroscop

            # Verificăm dacă unghiul țintă a fost atins (cu o toleranță de 1 grad)
            if abs(currentAngle - targetAngle) < tolerance:
                break  # Ieșim din buclă când suntem suficient de aproape de unghiul țintă

            if currentAngle < 0:
                # Dacă unghiul curent este negativ, facem robotul să vireze într-o direcție
                self.drive(-speed1, speed2)
            else:
                # Dacă unghiul curent este pozitiv, facem robotul să vireze în direcția opusă
                self.drive(speed1, -speed2)

    def straightWithGyro(self, distance: int, power: int) -> None:
        """
        Mărește distanța parcursă pe o linie dreaptă, corectând direcția cu ajutorul giroscopului.
        
        Parametri:
        - distance: distanța pe care robotul trebuie să o parcurgă (în unități corespunzătoare).
        - power: puterea (viteza) motoarelor pentru deplasare.
        """
        
        previousAngle = self.gyro.angle() 
        previousDistanceTravelled = self.dr.angle() 
        
        while True:
            distanceTravelled = self.dr.angle() - previousDistanceTravelled
            
            if abs(distanceTravelled) >= distance:
                break

            correction = self.gyro.angle() - previousAngle
            self.drive(power - correction, power + correction)
            
            previousAngle = self.gyro.angle()
            previousDistanceTravelled = self.dr.angle()  

        self.stop()