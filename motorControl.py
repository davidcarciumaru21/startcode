#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from robot import Robot 

# ************ VALUES AND OBJECTS ************

ev3 = EV3Brick()

# Crearea obiectului robotului și setarea parametrilor săi
nemo = Robot(49.5, 113)
nemo.d.settings(1000, 1000, 1000, 1000)  # Setarea vitezei și accelerației

# Variabilă pentru modul de funcționare (0 = DriveTrain, 1 = ArmMotors)
mode = 0

#*********** STATUS ***********

def displayStatus(mode):
    """
    Afișează pe ecranul EV3 modul curent de funcționare și instrucțiuni.
    """
    ev3.screen.clear()  # Eliberează ecranul pentru noul afișaj
    
    if mode == 0:
        ev3.screen.draw_text(0, 0, "Mode: Drive", Color.BLACK)
        ev3.screen.draw_text(0, 30, "Use arrows to", Color.BLACK)
        ev3.screen.draw_text(0, 50, "to control drive", Color.BLACK)
    elif mode == 1:
        ev3.screen.draw_text(0, 0, "Mode: Arm", Color.BLACK)
        ev3.screen.draw_text(0, 30, "Use arrows", Color.BLACK)
        ev3.screen.draw_text(0, 50, "to control arms", Color.BLACK)

    ev3.screen.draw_text(0, 80, "Press Center to", Color.BLACK)
    ev3.screen.draw_text(0, 100, "switch", Color.BLACK)
    wait(50)


#*********** MOTOR CONTROL ***********

def motorControl():
    """
    Controlează motoarele robotului în funcție de butoanele apăsate.
    """
    global mode 
    
    if mode == 0:  # Modul de control al sasiului
        if Button.UP in ev3.buttons.pressed():
            nemo.dr.run(1000)  # Deplasare motor dreapta înainte
        elif Button.DOWN in ev3.buttons.pressed():
            nemo.dr.run(-1000)  # Deplasare motor dreapta înapoi
        else:
            nemo.dr.run(0)  # Oprire

        if Button.RIGHT in ev3.buttons.pressed():
            nemo.st.run(1000)  # Deplasare motor stânga înainte
        elif Button.LEFT in ev3.buttons.pressed():
            nemo.st.run(-1000)  # Deplasare motor stânga înapoi
        else:
            nemo.st.run(0)  # Oprire 
    
    elif mode == 1:  # Modul de control al bratelor
        if Button.UP in ev3.buttons.pressed():
            nemo.bratDr.run(1000)  # Deplasare motor braț dreapta înainte
        elif Button.DOWN in ev3.buttons.pressed():
            nemo.bratDr.run(-1000)  # Deplasare motor braț dreapta înapoi
        else:
            nemo.bratDr.run(0)  # Oprire braț

        if Button.RIGHT in ev3.buttons.pressed():
            nemo.bratSt.run(1000)  # Deplasare motor braț stânga înainte
        elif Button.LEFT in ev3.buttons.pressed():
            nemo.bratSt.run(-1000)  # Deplasare motor braț dreapta înapoi
        else:
            nemo.bratSt.run(0)  # Oprire braț

    # Schimbarea modului de operare la apăsarea butonului centru
    if Button.CENTER in ev3.buttons.pressed():
        mode = 1 if mode == 0 else 0  
        wait(300)  # Întârziere pentru a evita schimbarea rapidă accidentală
    
    displayStatus(mode)  # Afișează noul mod pe ecran

#*********** MAIN LOOP ***********

def main():
    """
    Bucle principală care controlează robotul pe baza intrărilor de la butoane.
    """
    global mode  

    while True:
        motorControl()  # Apelarea funcției de control al motoarelor
        wait(50)

# Pornirea programului
main()