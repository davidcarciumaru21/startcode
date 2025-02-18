#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from missions import runs, ev3, nemo 
from logger import startLogging  # Importăm funcția de logging
import _thread
from additionalTools import toolList

# ************ VALUES AND FUNCTIONS ************

# Inițializăm runCounter-ul și pornim înregistrare datelor
runCounter = 1  
toolCounter = 0
running = 0
startLogging()

# Funcție pentru actualizarea ecranului cu valoarea lui runCounter
def updateScreen():
    global runCounter
    global toolCounter
    if toolCounter == 0:
        ev3.screen.clear()  # Clear the screen

        ev3.screen.draw_text(
            (ev3.screen.width - len("run " + str(runCounter)) * 6) // 2,  
            ev3.screen.height // 2 - 20, 
            "run " + str(runCounter),
            Color.BLACK, None
        ) 

        ev3.screen.draw_text(
            (ev3.screen.width - len(str(runs[(runCounter - 1)].data)) * 6) // 2,  
            ev3.screen.height // 2, 
            str(runs[(runCounter - 1)].data),
            Color.BLACK, None
        )
    else:
        ev3.screen.clear()  # Clear the screen

        ev3.screen.draw_text(
            (ev3.screen.width - len("run " + str(toolCounter)) * 6) // 2 - len("run " + str(toolCounter)) * 6 // 2,  
            ev3.screen.height // 2 - 20, 
            (toolList[(toolCounter - 1)].name),
            Color.BLACK, None
        ) 

def logrunCounterAndRunner() -> None:
    """
    Scrie suma dintre runCounter și running într-un fișier de log.
    """
    with open("logrunCounterAndRunner.txt", 'w') as runCounterFile:
        runCounterFile.write(str(runCounter) + str(running))

# Afișăm valoarea inițială a lui runCounter
updateScreen()

# ************ MAIN ************

# Bucla principală a programului
while True:
    logrunCounterAndRunner()
    # Verificăm dacă butonul UP este apăsat
    if Button.UP in ev3.buttons.pressed():  
        if toolCounter == 0:
            if runCounter < len(runs):  # Ne asigurăm că nu depășim limita listei
                runCounter += 1  # Incrementăm runCounter-ul
            updateScreen()  # Actualizăm ecranul
            wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    # Verificăm dacă butonul DOWN este apăsat
    elif Button.DOWN in ev3.buttons.pressed():  
        if toolCounter == 0:
            if runCounter > 1:  # Ne asigurăm că nu scădem sub 1
                runCounter -= 1  # Decrementăm runCounter-ul
                updateScreen()  # Actualizăm ecranul
                wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    elif Button.RIGHT in ev3.buttons.pressed():  
        if toolCounter < len(toolList):  # Ne asigurăm că nu depășim limita listei
            toolCounter += 1  # Incrementăm runCounter-ul
        updateScreen()  # Actualizăm ecranul
        wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    elif Button.LEFT in ev3.buttons.pressed():  
        if toolCounter > 0:  # Ne asigurăm că nu depășim limita listei
            toolCounter -= 1  # Incrementăm runCounter-ul
        updateScreen()  # Actualizăm ecranul
        wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    # Verificăm dacă senzorul touch este apăsat
    elif nemo.touch.pressed():  
        if toolCounter == 0:
            runs[(runCounter - 1)].mission()
        else: 
            toolList[(toolCounter - 1)].tool()
        wait(100)  # Pauză pentru a evita activarea multiplă

    wait(100)  # Pauză generală pentru eficiență