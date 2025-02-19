#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

import time  # Importă modulul de gestionare a timpului
from pybricks.tools import DataLog  # Importă funcționalitatea de înregistrare a datelor
from globalValues import nemo, ev3  # Importă obiectele necesare pentru controlul robotului
import _thread  # Importă modulul pentru a lucra cu fire de execuție
from pybricks.hubs import EV3Brick  # Importă hub-ul EV3Brick
from pybricks.tools import wait, StopWatch, DataLog  # Importă instrumente suplimentare pentru gestionarea timpului și înregistrarea datelor

# ************ VALUES AND OBJECTS ************

# Inițializăm un obiect DataLog pentru înregistrarea datelor relevante.
# Acestea includ unghiurile roților, unghiurile brațelor, tensiunea bateriei și unghiul senzorului de giroscop.
loger = DataLog(
    'drAngle',  # Unghiul roții dreapta
    'stAngle',  # Unghiul roții stânga
    'bratdrAngle',  # Unghiul brațului drept
    'bratstAngle',  # Unghiul brațului stâng
    'voltage',  # Tensiunea bateriei
    'gyro',  # Unghiul giroscopului
    name='log',  # Numele fișierului de logare
    timestamp=False,  # Nu includem timestamp în fișier
    extension='csv',  # Extensia fișierului de logare
    append=False  # Nu adăugăm la un fișier existent, ci creăm unul nou
)

# ************ MAIN ************

# Funcție pentru rularea unui thread care colectează și înregistrează datele senzorilor
def logDataThread() -> None:
    """
    Această funcție rulează într-un thread separat pentru a colecta și înregistra date de la senzori
    și componente ale robotului la intervale regulate.
    """
    while True:
        try:
            # Înregistrăm valorile relevante ale senzorilor și componentelor robotului
            loger.log(
                nemo.dr.angle(),  # Unghiul roții dreapta
                nemo.st.angle(),  # Unghiul roții stânga
                nemo.bratDr.angle(),  # Unghiul brațului drept
                nemo.bratSt.angle(),  # Unghiul brațului stâng
                ev3.battery.voltage() / 1000,  # Tensiunea bateriei EV3 în volți (divizăm la 1000 pentru a obține volți)
                nemo.gyro.angle(),  # Unghiul giroscopului
            )
            wait(100)  # Așteptăm 100ms înainte de a înregistra din nou
        except:
            break
        wait(100)  # Așteptăm 100ms între fiecare înregistrare pentru a reduce încărcarea procesorului

# Funcție pentru pornirea procesului de înregistrare a datelor
def startLogging():
    """
    Această funcție pornește un thread nou care rulează funcția `logDataThread`.
    Este folosită pentru a începe procesul de logare a datelor.
    """
    _thread.start_new_thread(logDataThread, ())  # Pornim thread-ul care colectează datele