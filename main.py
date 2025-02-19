#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from missions import ev3, nemo 
from logger import startLogging  
import _thread
from additionalTools import toolList
from run import blueRuns, redRuns

# ************ MAIN ************

base = "red"

def displayBase() -> None:
    global base
    ev3.screen.clear()  # Clear the screen

    ev3.screen.draw_text(
        (ev3.screen.width - len(base) * 6) // 2,  
        ev3.screen.height // 2 - 20, 
        base,
        Color.BLACK, None
    ) 

    ev3.screen.draw_text(
        (ev3.screen.width - len(str(nemo.gyro.angle())) * 6) // 2,  
        ev3.screen.height // 2, 
        nemo.gyro.angle(),
        Color.BLACK, None
    ) 

while True:
    displayBase()
    detectedColour = nemo.colourBt.color()
    
    if base == "red":
        for run in redRuns:
            if detectedColour == run.colour:
                run.mission()
    elif base == "blue":
        for run in blueRuns:
            if detectedColour == run.colour:
                run.mission()

    for tool in toolList:
        if tool.colour == detectedColour:  
            tool.tool()

    if Button.RIGHT in ev3.buttons.pressed(): 
        if base == "red":
            base = "blue"

    if Button.LEFT in ev3.buttons.pressed(): 
        if base == "blue":
            base = "red" 
    
    wait(100)  