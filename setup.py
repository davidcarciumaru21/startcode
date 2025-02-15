#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread
from errors import *

# ************ ROBOT CLASS ************
class Robot:
    def __init__(self, WHEELDIAMETER: float, AXLETRACK: float) -> None:
        self.WHEELDIAMETER = WHEELDIAMETER #! constanta. Nu o modifica!
        self.AXLETRACK = AXLETRACK #! constanta. Nu o modifica!

        self.st = self.initMotor(Port.A, "Left motor", Direction.CLOCKWISE)
        self.dr = self.initMotor(Port.D, "Right motor", Direction.CLOCKWISE)
        self.bratSt = self.initMotor(Port.C, "Left arm motor")
        self.bratDr = self.initMotor(Port.B, "Right arm motor")

        # Initialize sensors
        self.touch = self.initSensor(TouchSensor, Port.S4, "Touch sensor")
        self.gyro = self.initSensor(GyroSensor, Port.S1, "Gyro sensor")

        # Initialize drive base
        self.d = DriveBase(self.st, self.dr, self.WHEELDIAMETER, self.AXLETRACK)


        # Initialize drive base
        self.d = DriveBase(self.st, self.dr, self.WHEELDIAMETER, self.AXLETRACK)

        # Thread control locks
        self.lock0 = _thread.allocate_lock()
        self.lock1 = _thread.allocate_lock()
        self.lock2 = _thread.allocate_lock()
        self.lock3 = _thread.allocate_lock()
        self.threadStopFlag = False

        # List of motors for easy access
        self.motorList = [self.st, self.dr, self.bratSt, self.bratDr]

    # ************ INITIALIZATION METHODS ************
    def initMotor(self, port: Port, name: str, direction=Direction.CLOCKWISE) -> Motor:
        """Initialize a motor and handle errors if it fails."""
        try:
            return Motor(port, direction)
        except Exception as e:
            raise UnableToFindMotor(name)

    def initSensor(self, sensorClass: object, port: Port, name: str) -> object:
        """Initialize a sensor and handle errors if it fails."""
        try:
            return sensorClass(port)
        except Exception as e:
            raise UnableToFindSensor(name)

    # ************ MOVEMENT CONTROL ************
    def stopRobot(self) -> None:
        """Stop all motors."""
        for motor in self.motorList:
            motor.stop()

    def holdRobot(self) -> None:
        """Hold all motors in place."""
        for motor in self.motorList:
            motor.hold()

    # ************ THREAD CONTROL ************
    def startThreads(self) -> None:
        """Allow threads to run."""
        self.threadStopFlag = False

    def stopThreads(self) -> None:
        """Stop all threads."""
        self.thread_stop_flag = True

    # ************ THREADED MOVEMENTS ************
    def runThread(self, function: callable, args: tuple) -> None:
        """Start a new thread if threads are not stopped."""
        if not self.thread_stop_flag:
            _thread.start_new_thread(function, args)

    def straightThreaded(self, distance: int, lock: object) -> None:
        """Move the robot straight in a threaded manner."""
        with lock:
            self.drive_base.straight(distance)

    def runMotorByTimeThreaded(self, speed: int, duration: int, motor: Motor, lock: object) -> None:
        """Run a motor for a specific duration in a threaded manner."""
        with lock:
            motor.run_time(speed, duration)

    def runMotorByAngleThreaded(self, speed: int, angle: int, motor: Motor, lock: object) -> None:
        """Run a motor to a specific angle in a threaded manner."""
        with lock:
            motor.run_angle(speed, angle)

    # ************ DRIVETRAIN MOVEMENT ************

    def drive(self, powerDr: int, powerSt: int) -> None:
        self.dr.run(powerDr)
        self.st.run(powerSt)
    
    def runDr(self, powerDr):
        self.dr.run_until_stalled(powerDr)

    def runSt(self, powerSt):
        self.st.run_until_stalled(powerSt)

    def driveUntilStalled(self, powerDr: int, powerSt: int) -> None:
        _thread.start_new_thread(self.runDr, (powerDr,)) 
        _thread.start_new_thread(self.runSt, (powerSt,)) 

    # ************ GYRO-ASSISTED MOVEMENT ************
    
    def gotoGyro(self, Kp: float, Ki: float, Kd: float, targetAngle: int, tolerance: int = 1) -> None:
        previousError = 0
        integral = 0

        while True:
            currentAngle = self.gyro.angle()  
            error = targetAngle - currentAngle
            integral += error * 0.01  
            
            derivative = (error - previousError) / 0.01  
            output = Kp * error + Ki * integral + Kd * derivative  

            self.drive(-output, output)

            previousError = error

            if abs(error) <= tolerance:
                break