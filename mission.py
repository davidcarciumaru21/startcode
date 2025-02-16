class Mission:
    """ Prin intermediul acestei clase putem crea un obiect misiune 
        cu care punem afisa diferite informatii pe ecranul robotului """
    def __init__(self, mission: callable, data: str) -> None:
        self.mission = mission
        self.data = data

    def __str__(self) -> str:
        return str(self.data)