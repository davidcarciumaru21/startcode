blueMRuns = []
redRuns = []

class Run:
    """ 
    Această clasă permite crearea unui obiect de tip misiune.
    
    Atributele clasei:
    - mission: un obiect de tip callable care reprezintă misiunea de executat.
    - colour: un obiect care reprezintă culoarea asociată misiunii, folosit pentru a personaliza afișarea.
    - base: baza de pornire a misiunii.
    """
    
    def __init__(self, mission: callable, colour: object, base: str) -> None:
        """
        Constructorul clasei Run. Creează un obiect de tip misiune cu datele specificate.
        
        Parametri:
        - mission: funcția (sau orice alt obiect callable) care va fi executată ca parte a misiunii.
        - colour: culoarea asociată misiunii.
        - base: baza din care această misiune va fi rulată ("red" sau "blue").
        """
        self.mission = mission  # Atribuirea funcției sau metodei care reprezintă misiunea
        self.colour = colour  # Atribuirea culorii misiunii
        self.base = base  # Setarea bazei de pornire a misiunii

        self.selectList()

    def __str__(self) -> str:
        """
        Reprezentarea sub formă de șir a obiectului Mission.
        Această metodă returnează culoarea misiunii atunci când obiectul este convertit într-un șir de caractere.
        
        Returnează:
        - Șirul ce reprezintă culoarea misiunii.
        """
        return str(self.colour)  # Returnează culoarea misiunii 

    def selectList(self) -> None:
        """
        Adaugă obiectul misiunii în lista corespunzătoare, în funcție de baza specificată.
        """
        match self.base:
            case "red":
                redMissions.append(self)
            case "blue":
                blueMissions.append(self)

    @classmethod
    def registerMission(cls, color: object, base: str) -> callable:
        """
        Decorator pentru a înregistra automat o misiune în lista corespunzătoare.
        
        Parametri:
        - description: Descrierea misiunii.
        - color: Culoarea asociată misiunii.
        - base: Baza de pornire ("red" sau "blue").
        """
        def decorator(func):
            missionObj = cls(func, color, base)  # Creează un obiect Run
            return func  # Returnează funcția originală fără modificări
        return decorator