class UnableToFindMotor(Exception):
    """
    Excepție personalizată pentru cazul în care un motor nu este găsit.
    """
    def __init__(self, motor):
        self.message = "Unable to find " + motor  # Mesaj de eroare personalizat
        super().__init__(self.message)  # Apelul constructorului clasei părinte

class UnableToFindSensor(Exception):
    """
    Excepție personalizată pentru cazul în care un senzor nu este găsit.
    """
    def __init__(self, sensor):
        self.message = "Unable to find " + sensor  # Mesaj de eroare personalizat
        super().__init__(self.message)  # Apelul constructorului clasei părinte
