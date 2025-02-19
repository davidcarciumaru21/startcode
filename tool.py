class Tool:
    def __init__(self, tool: callable, colour: object) -> None:
        """
        Constructorul clasei Tool.

        Args:
            tool (callable): Funcția sau metoda care reprezintă unealta sau acțiunea.
            colour (object): Culoarea uneltei, reprezentată printr-un obiect.
        """
        self.tool = tool  # Atribuirea funcției sau metodei care reprezintă efectiv unealta
        self.colour = colour  # Atribuirea culorii uneltei, care poate fi utilizată pentru a descrie uneltele vizual

    def __str__(self) -> str:
        """
        Returnează o reprezentare sub formă de str a obiectului Tool.
        """
        return str(self.colour)  # Returnează culoarea tool-ului
