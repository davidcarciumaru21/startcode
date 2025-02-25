class Run:
    """
    Clasa `Run` permite crearea unui obiect de tip misiune.
    
    Atribute:
    - mission: Funcția (sau orice alt obiect `callable`) care va fi executată ca parte a misiunii.
    - colour: Culoarea asociată misiunii.
    - base: Baza din care această misiune va fi rulată ("red" sau "blue").
    - runList: Lista în care va fi adăugată misiunea (ex. `redRuns` sau `blueRuns`).
    """

    def __init__(self, mission: callable, colour: object, runList: list) -> None:
        """
        Constructorul clasei `Run`. Creează un obiect de tip misiune cu datele specificate.
        
        Parametri:
        - mission: Funcția care reprezintă misiunea.
        - colour: Culoarea asociată misiunii.
        - base: Baza de pornire ("red" sau "blue").
        - runList: Lista în care trebuie adăugată această misiune.
        """
        self.mission = mission  # Salvăm funcția de execuție a misiunii
        self.colour = colour  # Salvăm culoarea misiunii
        self.runList = runList  # Referință la lista în care va fi adăugată misiunea
        self.selectList()  # Adăugăm automat misiunea în lista corespunzătoare

    def selectList(self) -> None:
        self.runList.append(self)  # Adaugă misiunea în lista specificată

    @classmethod
    def registerMission(cls, color: object, runList: list) -> callable:
        """
        Decorator pentru înregistrarea automată a unei misiuni într-o listă.

        Parametri:
        - color: Culoarea asociată misiunii.
        - base: Baza de pornire ("red" sau "blue").
        - runList: Lista în care va fi adăugată misiunea.

        Returnează:
        - Un decorator care creează și înregistrează automat un obiect `Run`.
        """
        def decorator(func: callable) -> callable:
            obj = Run(func, color, runList)  # Creează și înregistrează un obiect `Run`
            return func  # Returnează funcția originală fără modificări
        return decorator
