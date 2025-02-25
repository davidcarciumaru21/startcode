class Base:
    """
    Clasa `Base` reprezintă o bază de start pentru robot.
    Fiecare bază are un nume și o listă de misiuni asociate.
    """

    def __init__(self, name: str) -> None:
        """
        Inițializează o bază cu un nume și o listă goală de misiuni.

        name: Numele bazei
        """
        self.name = name  # Numele bazei
        self.missions = []  # Listă de misiuni asociate bazei (inițial goală)
