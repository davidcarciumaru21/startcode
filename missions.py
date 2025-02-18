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
nemo02.d.settings(2000, 2000, 500, 500)

nemo03 = Robot(49.5, 115)
nemo03.d.settings(2000, 2000, 2000, 2000)

nemo04 = Robot(49.5, 115)
nemo04.d.settings(2000, 2000, 2000, 2000)

# ************ RUNS ************

def run01(): #colectare stanga
    #nemo01.bratDr.run_angle(-1000, 200)
    nemo01.d.straight(450)
    nemo01.bratDr.run_angle(-150, 150)
    #curba
    nemo01.d.reset()
    while nemo01.d.distance() > -400:
        nemo01.d.drive(-300, 20)
    nemo01.d.straight(-5)
    nemo01.d.stop()
    
    

def run02(): #recif, rechin, scubi
    wait(200)
    nemo02.d.turn(5)
    nemo02.d.straight(710)
    #nemo02.d.straight(60)
    #nemo02.d.turn(5)
    nemo02.bratDr.run_angle(800, 600)
    nemo02.bratDr.run_angle(-800, 430)
    #nemo02.d.turn(-5)
    nemo02.d.straight(-30)
    nemo02.bratDr.run_angle(800, 40)
    

    wait(100)
    #nemo02.bratDr.run_angle(800, 210) #pozitie colectare scubi
    wait(100)
    nemo02.d.turn(-95)
    wait(100)
    nemo02.bratSt.run_angle(600, 500) #brat jos sub recif
    
    
    nemo02.d.straight(105) #la recif
    nemo02.bratDr.run_angle(-150, 170) #luat scubi
    wait(100)
    nemo02.d.turn(7)
    nemo02.bratSt.run_angle(-350, 610) #ridicare recif
    #wait(100)
    nemo02.bratSt.run_angle(600, 170)
    

    nemo02.d.straight(-100)
    nemo02.d.turn(97)
    nemo02.d.straight(50)
    

    nemo02.bratDr.run_angle(200, 220) #dus scubi
    nemo02.d.straight(-70)
    nemo02.d.turn(-10)
    nemo02.bratSt.run_angle(600, 470)
    nemo02.bratSt.run_angle(-1000, 600)
    #nemo02.d.straight(-830)
    nemo02.d.reset()
    while nemo02.d.distance() > -700:
        nemo02.d.drive(-300, 10)
    nemo02.d.straight(-5)
    nemo02.d.stop()
    
    '''
    nemo02.d.turn(-80)
    nemo02.d.straight(30)
    nemo02.d.turn(80)
    nemo02.d.straight(20)
    
    nemo02.bratSt.run_angle(500, 500)
    nemo02.bratDr.run_angle(500, 300)
    wait(100)
    nemo02.bratSt.run_angle(-500, 500)
    nemo02.bratDr.run_angle(-500, 300)
    nemo02.d.straight(-700)
    
    
    nemo02.d.straight(-600)
    
    nemo02.d.straight(-100)
    nemo02.d.turn(20)
    nemo02.d.straight(-700)
    nemo02.stopRobot()'''

def run03(): #catarg, dus rechin, nava, colectare trident si un crevete
    wait(200)
    nemo03.d.straight(200)
    nemo03.d.turn(90)
    nemo03.d.straight(200)
    nemo03.d.turn(-45)

def run04():#barca, anglerfish, verde rotund, colectare dreapta, baza dreapta
    wait(200)
    nemo04.d.straight(200)
    nemo04.d.turn(90)
    nemo04.d.straight(800)
    nemo04.d.turn(45)

# Lista de run-uri pe care robotul le poate face

run01Obj = Mission(run01, "nimic", Color.GREEN)
run02Obj = Mission(run02, "recif, rechin", Color.YELLOW)
run03Obj = Mission(run03, "recif", Color.WHITE)
run04Obj = Mission(run04, "barca", Color.BLUE)

blueRuns = []
redRuns = [run01Obj, run02Obj, run03Obj, run04Obj]