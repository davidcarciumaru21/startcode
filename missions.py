#!/usr/bin/env pybricks-micropython

#IMPORTS**********

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from setup import Robot

#DECLARARE**********

nemo01 = Robot(49.5, 115)
nemo01.d.settings(2000, 2000, 2000, 2000)

nemo02 = Robot(49.5, 115)
nemo02.d.settings(2000, 2000, 2000, 2000)

nemo03 = Robot(49.5, 115)
nemo03.d.settings(2000, 2000, 2000, 2000)

#RUN-URILE**********

def run01(): #colectare stanga
    wait(200)


def run02(): #recif, rechin, scubi
    wait(200)
    nemo02.d.straight(650)
    nemo02.d.turn(-90)
    nemo02.d.straight(90) #la recif
    nemo02.d.straight(-100)
    nemo02.d.turn(40)
    nemo02.d.straight(290) #spre rechin
    nemo02.d.straight(-360)
    nemo02.d.turn(40)
    nemo02.d.straight(300) #misiunea verde
    nemo02.d.straight(-100)
    nemo02.d.turn(20)
    nemo02.d.straight(-700)
    nemo02.stopRobot()

def run03(): #colectare stanga
    wait(200)
    nemo03.d.straight(550)
    nemo03.d.turn(88)
    nemo03.d.straight(150) #ridicare catarg
    nemo03.d.straight(-50)
    nemo03.d.turn(70)
    nemo03.d.straight(420)
    nemo03.d.turn(-130)
    nemo03.d.straight(400) #spre nava
    #trident si crevete
    nemo03.d.straight(-600)