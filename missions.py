#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from mission import Mission

from setup import Robot 

# ************ GLOBAL VALUES ************

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

nemo04 = Robot(49.5, 115)
nemo04.d.settings(2000, 2000, 2000, 2000)

# ************ RUNS ************

def run01(): #colectare stanga
    wait(200)

def run02(): #recif, rechin, scubi
    wait(200)
    nemo02.d.straight(660)
    wait(100)
    nemo02.bratDr.run_angle(500, 250) #pozitie colectare scubi
    wait(100)
    nemo02.d.turn(-90)
    wait(100)
    nemo02.bratSt.run_angle(-200, 180) #brat jos sub recif
    
    
    nemo02.d.straight(60) #la recif
    nemo02.bratSt.run_angle(100, 170) #ridicare recif
    #nemo02.bratSt.run_angle(-100, 30)
    nemo02.bratDr.run_angle(-150, 80) #luat scubi

    nemo02.d.straight(-100)
    nemo02.d.turn(95)
    nemo02.d.straight(120)
    nemo02.bratDr.run_angle(150, 80) #dus scubi
    ''''nemo02.d.straight(-100)
    nemo02.d.turn(20)
    nemo02.d.straight(-700)
    nemo02.stopRobot()'''

def run03(): #catarg, dus rechin, nava, colectare trident si un crevete
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

def run04():#barca, anglerfish, verde rotund, colectare dreapta, baza dreapta
    wait(200)
    nemo04.d.straight(200)
    nemo04.d.turn(90)
    nemo04.d.straight(800)
    nemo04.d.turn(45)

# Lista de run-uri pe care robotul le poate face

run01Obj = Mission(run01, "nimic")
run02Obj = Mission(run02, "recif, rechin, scubi")
run03Obj = Mission(run03, "recif")
run04Obj = Mission(run04, "barca, angler fisch, verde rotund")

runs = [run01Obj, run02Obj, run03Obj, run04Obj]