class Mission:
    """ 
    Această clasă permite crearea unui obiect de tip misiune, 
    care poate fi folosit pentru a afisa informații pe ecranul robotului.
    
    Atributele clasei:
    - mission: un obiect de tip callable care reprezintă misiunea de executat.
    - data: un șir de caractere care conține datele relevante pentru misiune.
    - colour: un obiect care reprezintă culoarea asociată misiunii, folosit pentru a personaliza afișarea.
    """
    
    def __init__(self, mission: callable, data: str, colour: object) -> None:
        """
        Constructorul clasei Mission. Creează un obiect de tip misiune cu datele specificate.
        
        Parametri:
        - mission: funcția (sau orice alt obiect callable) care va fi executată ca parte a misiunii.
        - data: informațiile care vor fi afișate pentru utilizator (de exemplu, descrierea misiunii).
        - colour: culoarea care va fi asociată misiunii pentru afișare (de exemplu, pentru un afișaj colorat).
        """
        self.mission = mission  # Atribuirea funcției sau metodei care reprezintă misiunea
        self.data = data  # Atribuirea datelor asociate misiunii
        self.colour = colour  # Atribuirea culorii asociate misiunii

    def __str__(self) -> str:
        """
        Reprezentarea sub formă de șir a obiectului Mission. Această metodă returnează datele misiunii 
        atunci când obiectul este convertit într-un șir de caractere.
        
        Returnează:
        - Șirul ce reprezintă datele misiunii.
        """
        return str(self.data)  # Returnează datele misiunii sub formă de șir