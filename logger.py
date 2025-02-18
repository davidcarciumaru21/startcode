#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************

import time
from pybricks.tools import DataLog
from missions import nemo, ev3
import _thread
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog

# ************ VALUES AND OBJECTS ************

# Inițializăm un obiect DataLog pentru înregistrarea datelor relevante
loger = DataLog('drAngle',
                'stAngle',
                'bratdrAngle',
                'bratstAngle',
                'voltage',
                'gyro',
                name='log',
                timestamp=False,
                extension='csv',
                append=False)

# ************ MAIN ************

# Funcție pentru rularea unui thread care colectează și înregistrează date

def logDataThread() -> None:
    while True:
        try:
            # Înregistrăm datele senzorilor și ale componentelor robotului
            loger.log(
                nemo.dr.angle(),  # Unghiul roții dreapta
                nemo.st.angle(),  # Unghiul roții stânga
                nemo.bratDr.angle(),  # Unghiul brațului drept
                nemo.bratSt.angle(),  # Unghiul brațului stâng
                ev3.battery.voltage() / 1000,  # Tensiunea bateriei EV3 în volți
                nemo.gyro.angle(),  # Unghiul gyro
            )
            wait(100)
        except:
            # Dacă apare o eroare terminăm bucla
            break
        wait(100)  # Așteptăm 50ms înainte de următoarea înregistrare

# Funcție pentru pornirea procesului de înregistrare a datelor
def startLogging():
    _thread.start_new_thread(logDataThread, ())