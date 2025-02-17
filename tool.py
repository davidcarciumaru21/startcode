class Tool:
    def __init__(self, tool: callable, name: str) -> None:
        """
        Constructorul clasei tool.

        Args:
            tool (callable): Funcția sau metoda care reprezintă unealta sau acțiunea.
            name (str): Numele sau descrierea uneltei.
        """
        self.tool = tool  # Atribuirea funcției sau metodei care reprezintă unealta
        self.name = name  # Atribuirea numelui sau descrierii uneltei

    def __str__(self) -> str:
        """
        Returnează o reprezentare sub formă de șir a obiectului tool.

        Returns:
            str: Numele sau descrierea uneltei.
        """
        return str(self.name)  # Returnează numele uneltei sub formă de șir