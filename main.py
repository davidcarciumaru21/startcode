#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from missions import run01
from setup import Robot
from missions import nemo
from pybricks.tools import DataLog
import _thread

ev3 = EV3Brick()

senzorApasare = TouchSensor(Port.S3)

loger = DataLog('drAngle', 'stAngle', 'bratdrAngle', 'bratstAngle', name='log', timestamp=True, extension='csv', append=False)

def logDataThread():
    while True:
        loger.log(nemo.d.dr.angle, nemo.d.st.angle, nemo.d.bratDr.angle, nemo.d.bratSt.angle)
        wait(100) 

_thread.start_new_thread(logDataThread, ())

def update_screen(x):
    ev3.screen.clear()
    ev3.screen.draw_text(80, 50, str(x), Color.BLACK, None)

x = 1  
update_screen(x)
ev3.speaker.beep()

runs = [run01]

while True:
    if Button.UP in ev3.buttons.pressed():
        x = min(x + 1, len(runs)) 
        update_screen(x)
        wait(200) 
    elif Button.DOWN in ev3.buttons.pressed():
        x = max(x - 1, 1) 
        update_screen(x)
        wait(200)
    elif senzorApasare.pressed():
        if 0 <= x - 1 < len(runs):
            runs[x - 1]()
        wait(200)  

    wait(50)