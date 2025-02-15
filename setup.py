# ************ IMPORTS ************

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from errors import *

# ************ ROBOT CLASS ************
class Robot:
    def __init__(self, wheel_diameter: float, axle_track: float):
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.ev3 = EV3Brick()

        self.st = self.initMotor(Port.B, "Motor stanga", Direction.COUNTERCLOCKWISE)
        self.dr = self.initMotor(Port.C, "Motor dreapta", Direction.COUNTERCLOCKWISE)
        self.bratSt = self.initMotor(Port.A, "Motor brat stanga")
        self.bratDr = self.initMotor(Port.D, "Motor brat dreapta")
        
        self.senzorApasare = self.initSensor(TouchSensor, Port.S4, "Touch sensor")
        self.senzorGyro = self.initSensor(GyroSensor, Port.S1, "Gyro sensor")
        
        self.d = DriveBase(self.st, self.dr, self.wheel_diameter, self.axle_track)

    def initMotor(self, port: object, name: str, direction=Direction.CLOCKWISE):
        try:
            return Motor(port, direction)
        except:
            raise UnableToFindMotor(name)

    def initSensor(self, sensorClass: object, port: object, name: str):
        try:
            return sensorClass(port)
        except:
            raise UnableToFindSensor(name)

    def frana(self):
        self.d.dr.stop()
        self.d.st.stop()
        self.bratDr.stop()
        self.bratSt.stop()