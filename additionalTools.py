from missions import ev3, nemo
from tool import Tool

def resetGyro(threshold: int = 3) -> None:
    """
    Resetează unghiul gyro la 0 dacă valoarea acestuia depășește pragul.
    Emită un semnal sonor atunci când unghiul gyro depășește pragul, 
    pentru a avertiza utilizatorul că senzorul a suferit o abatere semnificativă.
    """

    # Variabila de avertizare pentru semnalul sonor
    warned = False

    # Verificăm dacă unghiul gyro depășește pragul
    if abs(nemo.gyro.angle()) > threshold and not warned:
        # Dacă abaterea este mai mare decât pragul și nu a fost deja emis un semnal sonor
        ev3.speaker.beep()  # Emitere semnal sonor pentru avertizare
        warned = True  # Setăm flag-ul warned la True pentru a nu emite un semnal sonor din nou

    # Dacă abaterea rămâne mai mare decât pragul și flag-ul warned este True, resetăm gyro
    elif abs(nemo.gyro.angle()) > threshold and warned:
        nemo.gyro.reset_angle(0)  # Resetăm unghiul gyro la 0 pentru a preveni o deriva permanentă

    # Dacă abaterea este sub prag, resetăm unghiul gyro
    else:
        nemo.gyro.reset_angle(0)  # Resetăm unghiul gyro la 0 pentru a asigura o valoare corectă

tool01Obj = Tool(resetGyro, "Reset gyro")

toolList = [tool01Obj]