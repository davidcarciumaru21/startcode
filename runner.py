#!/usr/bin/env pybricks-micropython

# ************ IMPORTS ************
from pybricks.parameters import Button, Color
from pybricks.tools import wait

from globalValues import ev3, nemo 
from additionalTools import toolList

class Runner:
    """
    Clasa Runner controlează execuția și afișarea bazei de start, selectarea uneltelor,
    pornirea misiunilor și gestionarea senzorilor/motoarelor pentru un robot LEGO EV3.
    """

    def __init__(self, startBase: str, bases: list) -> None:
        """
        Inițializează Runner cu baza de start și lista de baze disponibile.
        """
        self.startBase = startBase  # Baza curentă selectată
        self.counter = 0  # Indexul bazei curente în lista `bases`
        self.bases = bases  # Lista bazelor disponibile

    def getTextX(self, text: str) -> int:
        """
        Calculează poziția X pentru centrare pe ecranul EV3.
        Returnează 0 dacă textul depășește dimensiunea ecranului.
        """
        textWidth = len(text) * 6  # Fiecare caracter ocupă aproximativ 6 pixeli
        centeredX = (ev3.screen.width - textWidth) // 2

        return centeredX if centeredX + textWidth < ev3.screen.width else 0
        
    def separateText(self, text: str) -> list:
        """
        Desparte un text în cuvinte și le combină dacă textul nu încape pe o singură linie.
        """
        if self.getTextX(text) != 0:
            return text.split()  # Dacă textul încape, îl returnează separat pe cuvinte

        splitedText = text.split()

        while self.getTextX(" ".join(splitedText)) == 0:
            merged = False
            for idx in range(len(splitedText) - 1): 
                if self.getTextX(splitedText[idx]) != 0:
                    splitedText[idx] += " " + splitedText[idx + 1]  # Combină cuvintele
                    splitedText.pop(idx + 1)
                    merged = True
                    break  

            if not merged: 
                break  

        return splitedText

    def displayText(self, text: str, y: int = 0) -> None:
        """
        Afișează textul pe ecran, fie centrat, fie aliniat la stânga în funcție de rând.
        """
        separatedText = self.separateText(text)  

        for idx, words in enumerate(separatedText):
            xPos = self.getTextX(words) if idx == 0 else 0  # Primul rând este centrat
            ev3.screen.draw_text(
                xPos,
                20 * (idx + 1) if text == self.startBase.name else y,  # Determină poziția Y
                words,  
                Color.BLACK,
                None
            )

    def displayGyro(self, y: int) -> None:
        """
        Afișează unghiul giroscopului pe ecran.
        """
        self.displayText(str(nemo.gyro.angle()), y)

    def displayColourSensor(self, sensor: object, y: int) -> None:
        """
        Afișează culoarea detectată de senzorul de culoare.
        """
        self.displayText(str(sensor.colour()), y)

    def selectBase(self) -> None:
        """
        Selectează baza de start în funcție de butoanele apăsate pe EV3.
        """
        if Button.RIGHT in ev3.buttons.pressed() and self.counter < len(self.bases) - 1:
            self.counter += 1
            wait(100)
        elif Button.LEFT in ev3.buttons.pressed() and self.counter > 0:
            self.counter -= 1
            wait(100)
        self.startBase = self.bases[self.counter]  # Actualizează baza curentă

    def startRun(self) -> None:
        """
        Execută misiunea corespunzătoare culorii detectate de senzorul Bluetooth.
        """
        for run in self.startBase.missions:
            if run.colour == nemo.colourBt.color():
                run()  # Se presupune că `run` este o funcție apelabilă

    def stopMotorsWhenIdle(self) -> None:
        """
        Oprește motoarele dacă nu sunt active, pentru a preveni consumul inutil de energie.
        """
        for motor in nemo.motorList:
            try:
                motor.stop()
            except Exception as e:
                print(f"Unable to stop motor {motor}: {e}")  # Evităm eroarea de concatenare

    def selectTool(self) -> None:
        """
        Selectează și activează uneltele în funcție de culoarea detectată.
        """
        for tool in toolList:
            if tool.colour == nemo.colourBt.color():
                tool.tool()  # Se presupune că `tool.tool()` este o funcție apelabilă

    def run(self) -> None:
        """
        Buclează execuția principală:
        - Afișează baza curentă
        - Afișează unghiul giroscopului
        - Permite selectarea bazei
        - Selectează uneltele corespunzătoare
        - Execută misiunile corespunzătoare
        - Oprește motoarele când robotul este inactiv
        """
        while True:
            ev3.screen.clear()  # Șterge ecranul la începutul fiecărui ciclu

            self.displayText(self.startBase.name)
            lastBaseY = (len(self.startBase.name.split()) + 1) * 20  # Ajustare pe rânduri
            self.displayGyro(y=lastBaseY + 20)

            self.selectBase()
            self.selectTool()
            self.startRun()
            self.stopMotorsWhenIdle()
            wait(100)  # Așteptare pentru a evita rularea prea rapidă