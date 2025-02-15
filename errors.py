class UnableToFindMotor(Exception):
    def __init__(self, motor):
        self.message = "Unable to find " + motor
        super().__init__(self.message)

class UnableToFindSensor(Exception):
    def __init__(self, sensor):
        self.message = "Unable to find " + sensor
        super().__init__(self.message)