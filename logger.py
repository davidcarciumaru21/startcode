#!/usr/bin/env pybricks-micropython

import time
from pybricks.tools import DataLog
from missions import nemo
import _thread
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog

loger = DataLog('drAngle', 'stAngle', 'bratdrAngle', 'bratstAngle', 'voltage', 'gyro', 'button', name='log', timestamp=False, extension='csv', append=False)
nemo = Robot(49.5, 113)

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
        wait(50)

def startLogging():
    _thread.start_new_thread(logDataThread, ())