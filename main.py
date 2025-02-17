#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from missions import runs, ev3, nemo 
from logger import startLogging  # Importăm funcția de logging

# ************ VALUES AND FUNCTIONS ************

# Inițializăm counter-ul și pornim înregistrare datelor
counter: int = 1  
startLogging()

# Funcție pentru actualizarea ecranului cu valoarea lui counter
def updateScreen(counter):
    ev3.screen.clear()  # Clear the screen

    ev3.screen.draw_text(
        (ev3.screen.width - len("run " + str(counter)) * 6) // 2,  
        ev3.screen.height // 2 - 20, 
        "run " + str(counter),
        Color.BLACK, None
    ) 

    ev3.screen.draw_text(
        (ev3.screen.width - len(str(runs[(counter - 1)].data)) * 6) // 2,  
         ev3.screen.height // 2, 
        str(runs[(counter - 1)].data),
        Color.BLACK, None
    )


def logCounter():
    counterFile = open("counter.txt", 'w')
    counterFile.write(str(counter))
    counterFile.close()

# Afișăm valoarea inițială a lui counter
updateScreen(counter)

# ************ MAIN ************

# Bucla principală a programului
while True:
    nemo.stopDriveTrain()
    logCounter()
    # Verificăm dacă butonul UP este apăsat
    if Button.UP in ev3.buttons.pressed():  
        if counter < len(runs):  # Ne asigurăm că nu depășim limita listei
            counter += 1  # Incrementăm counter-ul
        updateScreen(counter)  # Actualizăm ecranul
        wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    # Verificăm dacă butonul DOWN este apăsat
    elif Button.DOWN in ev3.buttons.pressed():  
        if counter > 1:  # Ne asigurăm că nu scădem sub 1
            counter -= 1  # Decrementăm counter-ul
            updateScreen(counter)  # Actualizăm ecranul
            wait(100)  # Pauză pentru a evita multiple apăsări accidentale

    # Verificăm dacă senzorul touch este apăsat
    elif nemo.touch.pressed():  
        if 0 <= counter - 1 < len(runs):  # Ne asigurăm că indexul este valid
            runs[(counter - 1)].mission()  # Executăm funcția asociată numărului curent
        wait(100)  # Pauză pentru a evita activarea multiplă

    wait(100)  # Pauză generală pentru eficiență