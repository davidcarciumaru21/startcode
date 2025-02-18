#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

from pybricks.ev3devices import TouchSensor  # Importă senzorul de atingere
from pybricks.parameters import Button, Color  # Importă butoanele și culorile
from pybricks.tools import wait  # Importă funcția de așteptare
from missions import redRuns, blueRuns, ev3, nemo  # Importă misiunile și obiectele relevante
from logger import startLogging  # Importă funcția de logare (nu este folosită în acest fragment)
import _thread  # Importă modulul pentru execuția în fire de execuție
from additionalTools import toolList  # Importă lista de unelte suplimentare

# ************ MAIN ************

# Setează baza implicită (poate fi "red" sau "blue")
base = "red"

def displayBase() -> None:
    """
    Afișează pe ecran baza curentă și unghiul senzorului de giroscop al robotului.
    """
    global base  # Accesăm variabila globală base

    # Curățăm ecranul
    ev3.screen.clear()  

    # Afișăm textul pentru baza curentă
    ev3.screen.draw_text(
        (ev3.screen.width - len(base) * 6) // 2,  # Poziția X (centrat pe ecran)
        ev3.screen.height // 2 - 20,  # Poziția Y (centrat pe ecran)
        base,  # Textul de afișat
        Color.BLACK,  # Culoarea textului
        None  # Fără fundal
    )

    # Afișăm unghiul senzorului de giroscop
    ev3.screen.draw_text(
        (ev3.screen.width - len(str(nemo.gyro.angle())) * 6) // 2,  # Poziția X (centrat pe ecran)
        ev3.screen.height // 2,  # Poziția Y (sub textul anterior)
        nemo.gyro.angle(),  # Valoarea unghiului
        Color.BLACK,  # Culoarea textului
        None  # Fără fundal
    )

# Bucla principală a programului
while True:
    displayBase()  # Afișează baza curentă și unghiul senzorului de giroscop

    # Detectează culoarea curentă a obiectului
    detectedColour = nemo.colourBt.color()

    # Folosim 'match' în loc de 'if' pentru a compara valoarea 'base'
    match base:
        case "red":  # Dacă baza este "red"
            for run in redRuns:
                if detectedColour == run.colour:  # Dacă culoarea detectată corespunde cu misiunea
                    run.mission()  # Execută misiunea
        case "blue":  # Dacă baza este "blue"
            for run in blueRuns:
                if detectedColour == run.colour:  # Dacă culoarea detectată corespunde cu misiunea
                    run.mission()  # Execută misiunea

    # Verifică lista de unelte suplimentare și execută funcțiile lor
    for tool in toolList:
        if tool.colour == detectedColour:  # Dacă culoarea detectată corespunde cu unealta
            tool.tool()  # Execută funcția uneltei

    # Schimbă baza la apăsarea butonului drept
    if Button.RIGHT in ev3.buttons.pressed(): 
        match base:
            case "red":
                base = "blue"  # Schimbă la "blue" când este apăsat butonul drept
            case "blue":
                base = "red"  # Schimbă la "red" când este apăsat butonul drept
    
    # Așteaptă 100ms înainte de a repeta bucla
    wait(100)