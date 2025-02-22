#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.parameters import Button, Color
from pybricks.tools import wait
from globalValues import ev3, nemo 
from additionalTools import toolList
from missions import blueRuns, redRuns, greenRuns, runsList

# ************ MAIN ************

base = "red"
counter = 1

def displayBase() -> None:
    global base
    ev3.screen.clear()  # Clear the screen

    # Afiseaza / selecteaza baza
    ev3.screen.draw_text(
        (ev3.screen.width - len(base) * 6) // 2,  
        ev3.screen.height // 2 - 20, 
        base,
        Color.BLACK, None
    ) 

    # Afiseaza unghiul gyro
    ev3.screen.draw_text(
        (ev3.screen.width - len(str(nemo.gyro.angle())) * 6) // 2,  
        ev3.screen.height // 2, 
        nemo.gyro.angle(),
        Color.BLACK, None
    ) 

while True:
    try:
        nemo.dr.stop()
        nemo.st.stop()
    except:
        pass
    displayBase()
    detectedColour = nemo.colourBt.color()

    if base ==  "red":
        for run in redRuns:
            if detectedColour == run.colour:
                run.mission()
    elif base == "blue":
        for run in blueRuns:
            if detectedColour == run.colour:
                run.mission()
    
    elif base == "green":
        for run in greenRuns:
            if detectedColour == run.colour:
                run.mission()

    for tool in toolList:
        if tool.colour == detectedColour:
            tool.tool()

    if Button.RIGHT in ev3.buttons.pressed() and counter < len(runsList):
        counter += 1
        wait(100)

    if Button.LEFT in ev3.buttons.pressed() and counter > 1:
        counter -= 1
        wait(100)

    if counter == 1:
        base = "red"
    elif counter == 2:
        base = "blue"
    elif counter == 3:
        base = "green"

    wait(100)