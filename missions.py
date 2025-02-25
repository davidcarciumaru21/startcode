#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.parameters import Color, Stop
from pybricks.tools import wait
import _thread
from globalValues import ev3

from robot import Robot
from run import Run 

# ************ ROBOT OBJECTS ************

nemo00 = Robot(49.5, 115)
nemo00.d.settings(200, 200, 600, 600)

nemo01 = Robot(49.5, 115)
nemo01.d.settings(2000, 2000, 2000, 2000)

nemo02 = Robot(49.5, 115)
nemo02.d.settings(1000, 1000, 500, 500)

nemo03 = Robot(49.5, 115)
nemo03.d.settings(500, 300, 300, 300)

nemo04 = Robot(49.5, 115)
nemo04.d.settings(2000, 2000, 2000, 2000)

nemo05 = Robot(49.5, 115)
nemo05.d.settings(1000, 700, 700, 700)

nemo06 = Robot(49.5, 115)
nemo06.d.settings(800, 500, 500, 500)

nemo07 = Robot(49.5, 115)
nemo07.d.settings(700, 700, 700, 700)

nemo08 = Robot(49.5, 115)
nemo08.d.settings(130, 130, 130, 130)

redRuns = []
blueRuns = []
greenRuns = []

runsList = [redRuns, blueRuns, greenRuns]

# ************ RUNS ************

@Run.registerMission(Color.WHITE, redRuns)
def run01(): #colectare stanga
     #nemo01.bratDr.run_angle(-1000, 200)
    nemo01.d.straight(450)
    nemo01.bratDr.run_time(-100, 1200)
    #curba
    nemo01.d.reset()
    while nemo01.d.distance() > -440:
        nemo01.d.drive(-300, 20)
    nemo01.d.straight(-5)
    nemo01.d.stop()

@Run.registerMission(Color.BLUE, redRuns)
def run02(): #recif, rechin, scubi
    wait(200)
    nemo02.d.turn(5)
    nemo02.d.straight(710)
    #nemo02.d.straight(60)
    #nemo02.d.turn(5)
    nemo02.bratDr.run_angle(800, 710)
    nemo02.bratDr.run_angle(-800, 430)
    #nemo02.d.turn(-5)
    nemo02.d.straight(-30)
    #nemo02.bratDr.run_angle(800, 50)
    
    wait(100)
    #nemo02.bratDr.run_angle(800, 210) #pozitie colectare scubi
    wait(100)
    nemo02.d.turn(-93)
    wait(100)
    nemo02.bratSt.run_angle(600, 500) #brat jos sub recif
    
    nemo02.d.straight(115) #la recif
    nemo02.bratDr.run_angle(-150, 180) #luat scubi
    wait(100)
    nemo02.d.turn(8)
    
    nemo02.bratSt.run_angle(-350, 610) #ridicare recif
    #wait(100)
    nemo02.bratSt.run_angle(600, 200)
    
    nemo02.d.straight(-100)
    nemo02.d.turn(95)
    nemo02.d.straight(75)

    nemo02.bratDr.run_angle(200, 220) #dus scubi
    nemo02.d.straight(-60)
    nemo02.d.turn(-15)
    nemo02.bratSt.run_angle(600, 470)
    wait(100)
    nemo02.bratSt.run_angle(-1000, 600)
    #nemo02.d.straight(-830)
    nemo02.d.reset()
    while nemo02.d.distance() > -700:
        nemo02.d.drive(-300, 15)
    nemo02.d.straight(-5)
    nemo02.d.stop()
    nemo02.bratDr.run_angle(-200, 270)
    
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

@Run.registerMission(Color.GREEN,redRuns)
def run03(): #catarg, dus rechin, nava, colectare trident si un crevete
    wait(200)
    nemo03.d.straight(190)
    nemo03.d.turn(86)
    nemo03.d.straight(420)
    nemo03.d.turn(-52)
    nemo03.d.straight(240)
    nemo03.d.straight(-60)
    nemo03.bratDr.run_angle(-800, 180)
    nemo03.d.straight(-110)
    nemo03.bratDr.run_angle(-800, 100)
    nemo03.bratDr.run_angle(800, 300)
    nemo03.d.straight(110)
    nemo03.d.turn(90)
    nemo03.d.straight(-110)
    nemo03.d.turn(-40)
    nemo03.d.straight(-150)
    nemo03.d.turn(-50)
    nemo03.d.straight(-400)
    ''''
    nemo03.d.turn(-60)
    nemo03.d.straight(-400)
    
    nemo03.d.straight(-200)
    nemo03.d.turn(-30)
    nemo03.bratDr.run_angle(-800, 180)
    nemo03.d.straight(-100)
    nemo03.bratDr.run_angle(800, 180)
    nemo03.d.turn(-90)
    nemo03.d.straight(-400)
    
    
    
    
    nemo03.d.turn(-40)
    nemo03.d.straight(-100)
    nemo03.d.turn(-60)
    nemo03.d.straight(-500)'''
    

@Run.registerMission(Color.RED, redRuns)
def run04():#barca, anglerfish, verde rotund, colectare dreapta, baza dreapta
    wait(200)
    nemo04.bratDr.run_time(500, 500)
    nemo04.d.straight(200)
    nemo04.d.turn(88)
    #nemo04.straightWithGyro(2000, 500)
    nemo04.d.reset()
    while nemo04.d.distance() < 900:
        nemo04.d.drive(500, -8)
    nemo04.d.straight(-5)
    nemo04.d.stop()
    nemo04.bratDr.run_angle(-800, 140)
    nemo04.d.straight(370)
    nemo04.d.turn(40)
    nemo04.d.straight(-280)
    wait(100)
    nemo04.d.straight(440)

@Run.registerMission(Color.WHITE, blueRuns)
def run05(): #colectare 
    nemo05.d.straight(100)
    nemo05.d.turn(-20)
    nemo05.d.straight(300)
    nemo05.d.turn(40)
    nemo05.d.straight(150)
    nemo05.d.turn(-30)
    nemo05.d.straight(130)
    nemo05.d.turn(60)
    nemo05.d.straight(70)
    nemo05.d.turn(20)
    nemo05.d.straight(100)
    nemo05.d.straight(-200)
    nemo05.d.turn(-100)
    nemo05.d.straight(-700)
    
@Run.registerMission(Color.BLUE, blueRuns)
def run06(): #pinguin si sonar
    nemo06.d.straight(310)
    nemo06.d.turn(-25)
    nemo06.d.straight(430)#430
    nemo06.d.turn(70)
    nemo06.d.straight(200)#creveti in balena
    nemo00.d.straight(100)#creveti in balena
    wait(500)
    nemo06.d.straight(-270)
    nemo06.d.turn(-68)
    nemo06.d.straight(-150)#se duce la sonar
    nemo06.bratSt.run_time(-500, 900)
    nemo06.d.straight(120)
    nemo06.bratSt.run_angle(400, 70)#-800, 300
    nemo06.d.turn(23)
    nemo06.bratSt.run_time(-400, 500)#-800, 300
    nemo06.d.straight(-170)
    nemo06.bratSt.run_angle(500, 20)#-800, 10
    nemo06.d.turn(-40)
    nemo06.d.straight(380)
    nemo06.bratSt.run_angle(800, 90)
    nemo06.d.straight(-40)
    nemo06.bratSt.run_angle(800, 200)
    nemo06.d.straight(130)
    nemo06.d.turn(110)
    nemo06.d.straight(-340)
    nemo06.d.turn(-10)#face angler
    nemo06.d.straight(50)
    nemo06.d.turn(80)
    nemo06.d.straight(500)
    nemo06.d.turn(-20)
    nemo06.d.straight(500)
    '''
    nemo06.d.straight(-500)
    nemo06.d.turn(10)
    '''
    


    

@Run.registerMission(Color.GREEN, blueRuns)
def run07():
    nemo07.d.straight(400)
    nemo04.d.straight(-400)
    

@Run.registerMission(Color.RED, blueRuns)
def run08():
    nemo08.d.straight(180)
    nemo01.d.straight(-140)

globalLock = _thread.allocate_lock()

def threadStraight(angles):
    with globalLock:
        nemo07.d.straight(angles)

def threadBratDr(speed, angles):
    with globalLock:
        nemo07.bratDr.run_angle(speed, angles)
def threadBratSt(speed, angles):
    with globalLock:
        nemo07.bratSt.run_angle(speed, angles)