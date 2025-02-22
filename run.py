class Run:
    def __init__(self, mission: callable, colour: object, base: str, runList: list) -> None:
        self.mission = mission
        self.colour = colour
        self.base = base
        self.runList = runList
        self.selectList()

    def selectList(self) -> None:
        self.runList.append(self)

    @classmethod
    def registerMission(cls, color: object, base: str, runList: list) -> callable:
        def decorator(func: callable) -> callable:
            obj = Run(func, color, base, runList)  # Create and register a Run object
            return func  # Return the original function
        return decorator