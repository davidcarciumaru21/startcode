class ResetArmsPositions:
    def __init__(self, robot: object, bratDrDegrees: int, bratStDegrees: int, power: int = 1000) -> None:
        """
        Inițializează pozițiile brațelor robotului.

        Parametri:
        - robot (object): Referință către obiectul robotului.
        - bratDrDegrees (int): Unghiul în grade pentru motorul brațului drept.
        - bratStDegrees (int): Unghiul în grade pentru motorul brațului stâng.
        - power (int, implicit 1000): Puterea motoarelor brațelor.
        """
        self.robot = robot
        self.bratDrDegrees = bratDrDegrees
        self.bratStDegrees = bratStDegrees
        self.power = power

    def gotoPosition(self) -> None:
        """
        Mută brațele robotului la pozițiile specificate.
        """
        self.robot.runUntilStalledArms()
        
        self.resetArmsAngles()

        # Mișcă brațul drept la unghiul specificat
        self.robot.bratDr.run_angle(self.power, self.bratDrDegrees)

        # Mișcă brațul stâng la unghiul specificat
        self.robot.bratSt.run_angle(self.power, self.bratStDegrees)