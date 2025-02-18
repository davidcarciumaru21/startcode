class Tool:
    def __init__(self, tool: callable, name: str, colour: object) -> None:
        """
        Constructorul clasei Tool.

        Args:
            tool (callable): Funcția sau metoda care reprezintă unealta sau acțiunea.
            name (str): Numele sau descrierea uneltei.
            colour (object): Culoarea uneltei, reprezentată printr-un obiect (poate fi un șir, o valoare RGB etc.).
        """
        self.tool = tool  # Atribuirea funcției sau metodei care reprezintă efectiv unealta
        self.name = name  # Atribuirea numelui sau descrierii uneltei
        self.colour = colour  # Atribuirea culorii uneltei, care poate fi utilizată pentru a descrie uneltele vizual

    def __str__(self) -> str:
        """
        Returnează o reprezentare sub formă de șir a obiectului Tool.

        Returns:
            str: Numele sau descrierea uneltei.
        """
        return str(self.name)  # Returnează numele uneltei sub formă de șir
