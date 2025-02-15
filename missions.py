#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from setup import Robot 

# ************ GLOBAL VALUES ************

# Lista de run-uri pe care robotul le poate face
runs = [run01, run02, run03]

nemo = Robot(49.5, 113)
nemo.d.settings(2000, 2000, 2000, 2000)

ev3 = EV3Brick()

# ************ ROBOT OBJECTS ************

# Inițializăm instanțe ale robotului pentru fiecare run
nemo01 = Robot(49.5, 115)
nemo01.d.settings(2000, 2000, 2000, 2000)

nemo02 = Robot(49.5, 115)
nemo02.d.settings(2000, 2000, 2000, 2000)

nemo03 = Robot(49.5, 115)
nemo03.d.settings(2000, 2000, 2000, 2000)

# ************ RUNS ************

# colectare stânga
def run01():
    wait(200)

# recif, rechin, scubi
def run02():
    wait(200)
    nemo02.d.straight(650)  
    nemo02.d.turn(-90)  
    nemo02.d.straight(90)  # Ajunge la recif
    nemo02.d.straight(-100)
    nemo02.d.turn(40)
    nemo02.d.straight(290)  # Spre rechin
    nemo02.d.straight(-360)
    nemo02.d.turn(40)
    nemo02.d.straight(300)  # Misiunea verde
    nemo02.d.straight(-100)
    nemo02.d.turn(20)
    nemo02.d.straight(-700)
    nemo02.stopRobot()

# colectare stânga
def run03():
    wait(200)
    nemo03.d.straight(550)  
    nemo03.d.turn(88)  
    nemo03.d.straight(150)  # Ridicare catarg
    nemo03.d.straight(-50)
    nemo03.d.turn(70)
    nemo03.d.straight(420)
    nemo03.d.turn(-130)
    nemo03.d.straight(400)  # Spre navă
    # Trident și crevete
    nemo03.d.straight(-600)
