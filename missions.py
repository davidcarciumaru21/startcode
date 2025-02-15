#!/usr/bin/env pybricks-micropython

#***********IMPORTS***********

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from setup import Robot

#***********DECLARARE***********

nemo = Robot(49.5, 113)
nemo.d.settings(1000, 1000, 1000, 1000)

#***********RUN-URILE***********

def run01() -> None:
    nemo.gotoGyro(1, 0.01, 0.1, 90)