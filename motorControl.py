#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.robotics import DriveBase

from setup import Robot

#***********DECLARARE***********

ev3 = EV3Brick()  # FIXED: Initialize EV3 Brick
nemo = Robot(49.5, 113)
nemo.d.settings(1000, 1000, 1000, 1000)
mode = 0  # Global mode variable

#***********MOTORCONTROL***********

def motorControl():
    global mode  # FIXED: Declare mode as global to modify it

    if mode == 0:
        if Button.UP in ev3.buttons.pressed():
            nemo.dr.run(1000)  # FIXED: Use a reasonable speed
        elif Button.DOWN in ev3.buttons.pressed():
            nemo.dr.run(-1000)
        else:
            nemo.dr.run(0)

        if Button.RIGHT in ev3.buttons.pressed():
            nemo.st.run(1000)
        elif Button.LEFT in ev3.buttons.pressed():
            nemo.st.run(-1000)
        else:
            nemo.st.run(0)

    elif mode == 1:
        if Button.UP in ev3.buttons.pressed():
            nemo.bratDr.run(1000)  # FIXED: Use a reasonable speed
        elif Button.DOWN in ev3.buttons.pressed():
            nemo.bratDr.run(-1000)
        else:
            nemo.bratDr.run(0)

        if Button.RIGHT in ev3.buttons.pressed():
            nemo.bratSt.run(1000)
        elif Button.LEFT in ev3.buttons.pressed():
            nemo.bratSt.run(-1000)
        else:
            nemo.bratSt.run(0)

    if Button.CENTER in ev3.buttons.pressed():
        mode = 1 if mode == 0 else 0  
        wait(300)  

    wait(50) 

#***********MAIN***********

while True:
    motorControl()
