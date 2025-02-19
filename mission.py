class Mission:
    """ 
    Această clasă permite crearea unui obiect de tip misiune.
    
    Atributele clasei:
    - mission: un obiect de tip callable care reprezintă misiunea de executat.
    - colour: un obiect care reprezintă culoarea asociată misiunii, folosit pentru a personaliza afișarea.
    """
    
    def __init__(self, mission: callable, colour: object) -> None:
        """
        Constructorul clasei Mission. Creează un obiect de tip misiune cu datele specificate.
        
        Parametri:
        - mission: funcția (sau orice alt obiect callable) care va fi executată ca parte a misiunii.
        - data: informațiile care vor fi afișate pentru utilizator (de exemplu, descrierea misiunii).
        """
        self.mission = mission  # Atribuirea funcției sau metodei care reprezintă misiunea
        self.data = data  # Atribuirea datelor asociate misiunii

    def __str__(self) -> str:
        """
        Reprezentarea sub formă de șir a obiectului Mission. Această metodă returnează culoarea misiunii 
        atunci când obiectul este convertit într-un șir de caractere.
        
        Returnează:
        - Șirul ce reprezintă culoarea misiunii.
        """
        return str(self.colour)  # Returnează culoarea misiunii 