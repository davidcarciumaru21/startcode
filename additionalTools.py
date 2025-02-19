from globalValues import ev3, nemo  # Importă obiectele necesare pentru controlul robotului
from tool import Tool  # Importă clasa Tool pentru a crea un obiect Tool
from pybricks.parameters import Color  # Importă enumerația pentru culori
from pybricks.tools import wait  # Importă funcția wait pentru a adăuga pauze

warned = False  # Variabilă globală care indică dacă s-a emis deja un semnal sonor

def resetGyro(threshold: int = 3) -> None:
    """
    Resetează unghiul senzorului gyro la 0 dacă valoarea acestuia depășește pragul.
    Dacă unghiul depășește pragul, se emite un semnal sonor pentru avertizare.
    Odată avertizat utilizatorul, la următoarea verificare, gyro va fi resetat.
    """

    global warned  # Folosim variabila globală pentru a reține starea avertizării

    gyroAngle = abs(nemo.gyro.angle())  # Obținem valoarea absolută a unghiului gyro

    # Verificăm dacă unghiul gyro depășește pragul specificat
    if gyroAngle > threshold:
        if not warned:  # Dacă nu a fost emis deja un semnal sonor
            ev3.speaker.beep()  # Emitere semnal sonor pentru avertizare
            warned = True  # Setăm flag-ul warned la True pentru a evita semnalări repetate
            wait(100)  # Așteptăm 100ms pentru a nu emite semnalul sonor repetitiv
        else:
            nemo.gyro.reset_angle(0)  # Resetăm unghiul gyro la 0
            warned = False  # Resetăm flag-ul warned după resetarea unghiului

    else:
        # Dacă unghiul nu depășește pragul, resetăm gyro la 0 fără a emite semnal sonor
        nemo.gyro.reset_angle(0)
        warned = False  # Resetăm flag-ul warned în caz că unghiul nu este suficient de mare

# Creăm un obiect Tool care conține funcția resetGyro
tool01Obj = Tool(resetGyro, "Reset gyro", Color.RED)

# Lista de unelte care include funcția de resetare a senzorului gyro
toolList = [tool01Obj]  # Adăugăm uneltele într-o listă pentru a putea fi utilizate ulterior
