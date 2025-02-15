
#!/usr/bin/env pybricks-micropython

#*IMPORTS***********

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from setup import Robot

#*DECLARAM ROBOTII***********

nemo = Robot(49.5, 113)
nemo.settings(1000, 1000, 1000, 1000)
nemo.speacker.beep()

#*RUN-URILE***********

def run01(gradeS: int, vitezaE: int):
    nemo.d.straight(gradeS)
    nemo.bratD.run_angle(vitezaE, 70)
    nemo.d.straight(-gradeS)