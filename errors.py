class UnableToFindMotor(Exception):
    def __init__(self, motor):
        self.message = f"Unable to find motor {motor}"
        super().__init__(self.message)

class UnableToFindSensor(Exception):
    def __init__(self, sensor):
        self.message = f"Unable to find sensor {sensor}"
        super().__init__(self.message)