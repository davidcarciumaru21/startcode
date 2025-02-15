class UnableToFindMotor(Exception):
    """Exception raised when a motor cannot be found or initialized."""
    def __init__(self, motor: str) -> None:
        """
        Args:
            motor (str): The name or identifier of the motor that could not be found.
        """
        super().__init__(f"Unable to find motor: {motor}")


class UnableToFindSensor(Exception):
    """Exception raised when a sensor cannot be found or initialized."""
    def __init__(self, sensor: str) -> None:
        """
        Args:
            sensor (str): The name or identifier of the sensor that could not be found.
        """
        super().__init__(f"Unable to find sensor: {sensor}")