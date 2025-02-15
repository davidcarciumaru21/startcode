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
from missions import nemo
from pybricks.tools import DataLog
import _thread

ev3 = EV3Brick()

senzorApasare = TouchSensor(Port.S4)

loger = DataLog('drAngle', 'stAngle', 'bratdrAngle', 'bratstAngle', 'voltage', 'gyro', 'button', name='log', timestamp=False, extension='csv', append=False)

def logDataThread():  
    while True:
        try:
            loger.log(
                nemo.dr.angle(), 
                nemo.st.angle(),  
                nemo.bratDr.angle(),  
                nemo.bratSt.angle(),  
                ev3.battery.voltage() / 1000,  
                nemo.gyro.angle(), 
                nemo.touch.pressed() 
            )
        except:
           break
        
        wait(100)
       
_thread.start_new_thread(logDataThread, ())

def updateScreen(x):
    ev3.screen.clear()
    ev3.screen.draw_text(80, 50, str(x), Color.BLACK, None)

x = 1  
updateScreen(x)
ev3.speaker.beep()

runs = [run01]

while True:
    if Button.UP in ev3.buttons.pressed():
        x = min(x + 1, len(runs)) 
        updateScreen(x)
        wait(100) 
    elif Button.DOWN in ev3.buttons.pressed():
        x = max(x - 1, 1) 
        updateScreen(x)
        wait(100)
    elif senzorApasare.pressed():
        if 0 <= x - 1 < len(runs):
            runs[x - 1]()
        wait(100)  

    wait(50)