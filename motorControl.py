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

#*********** DECLARATION ***********

ev3 = EV3Brick()

nemo = Robot(49.5, 113)
nemo.d.settings(1000, 1000, 1000, 1000)

mode = 0

#*********** MOTOR CONTROL ***********

def displayStatus(mode):
    """
    Display the current mode and feedback on the screen with icons.
    """
    ev3.screen.clear()  # Clear the screen for the new display
    
    if mode == 0:
        ev3.screen.draw_text(10, 20, "Mode: Drive", Color.BLACK)
        ev3.screen.draw_image(50, 50, ImageFile.ARROW_UP) 
        ev3.screen.draw_text(10, 80, "Use arrows for movement", Color.BLACK)
    elif mode == 1:
        ev3.screen.draw_text(10, 20, "Mode: Arm", Color.BLACK)
        ev3.screen.draw_image(50, 50, ImageFile.TOOLBOX)  
        ev3.screen.draw_text(10, 80, "Use arrows to move arm", Color.BLACK)

    ev3.screen.draw_text(10, 100, "Press Center to Switch", Color.BLACK)
    wait(50)


def motorControl():
    """
    Control the robot's motors based on button inputs.
    """
    global mode 
    if mode == 0:
        if Button.UP in ev3.buttons.pressed():
            nemo.dr.run(1000)  
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
            nemo.bratDr.run(1000)  
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

    displayStatus(mode)  

#*********** MAIN LOOP ***********

def main():
    """
    Main loop to control the robot based on button inputs.
    """
    global mode

    while True:
        motorControl()  
        wait(50) 

main()