class Mission:
    """ 
    Această clasă permite crearea unui obiect de tip misiune, 
    care poate fi folosit pentru a afisa informații pe ecranul robotului.
    
    Atributele clasei:
    - mission: un obiect de tip callable care reprezintă misiunea de executat.
    - data: un șir de caractere care conține datele relevante pentru misiune.
    """
    
    def __init__(self, mission: callable, data: str) -> None:
     
        self.mission = mission  # Atribuirea funcției sau metodei care reprezintă misiunea
        self.data = data  # Atribuirea datelor asociate misiunii

    def __str__(self) -> str:
    
        return str(self.data)  # Returnează datele misiunii sub formă de șir
