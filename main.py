#!/usr/bin/env pybricks-micropython

# Import libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from missions import run01
from logger import startLogging 

ev3 = EV3Brick()
nemo = Robot(49.5, 113)

counter = 1  
runs = [run01]

startLogging()

def updateScreen(counter):
    ev3.screen.clear()  
    ev3.screen.draw_text(80, 50, str(counter), Color.BLACK, None) 

updateScreen(counter)

while True:
    if Button.UP in ev3.buttons.pressed():  
        if counter < len(runs): 
            counter += 1
        updateScreen(counter)  
        wait(100)

    elif Button.DOWN in ev3.buttons.pressed():  
        if counter > 1: 
            counter -= 1
            updateScreen(counter)
            wait(100)

    elif nemo.touch.pressed():  
        if 0 <= counter - 1 < len(runs):
            runs[counter - 1]()  
        wait(100) 

    wait(50) 