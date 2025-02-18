from missions import ev3, nemo
from tool import Tool
from pybricks.parameters import Color
from pybricks.tools import wait

warned = False  # Variabilă globală care indică dacă s-a emis deja un semnal sonor

def resetGyro(threshold: int = 3) -> None:
    """
    Resetează unghiul senzorului gyro la 0 dacă valoarea acestuia depășește pragul.
    Dacă unghiul depășește pragul, se emite un semnal sonor pentru avertizare.
    Odată avertizat utilizatorul, la următoarea verificare, gyro va fi resetat.
    """

    global warned  # Folosim variabila globală pentru a reține starea avertizării

    gyroAngle = abs(nemo.gyro.angle())  # Obținem valoarea absolută a unghiului gyro

    if gyroAngle > threshold:
        if not warned:  # Dacă nu a fost emis deja un semnal sonor
            ev3.speaker.beep()  # Emitere semnal sonor pentru avertizare
            warned = True  # Setăm flag-ul warned la True pentru a evita semnalări repetate
            wait(100)
        else:
            nemo.gyro.reset_angle(0)  # Resetăm unghiul gyro la 0
            warned = False  # Resetăm flag-ul warned după resetare

    else:
        nemo.gyro.reset_angle(0)
        warned = False  # Dacă unghiul este sub prag, resetăm starea avertizării

# Creăm un obiect Tool care conține funcția resetGyro
tool01Obj = Tool(resetGyro, "Reset gyro", Color.RED)

# Lista de unelte care include funcția de resetare a senzorului gyro
toolList = [tool01Obj]