
class pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon_cislo = telefon

    def __str__(self):
        return f"{self.jmeno}\t{self.prijmeni}\t\t{self.vek}\t{self.telefon_cislo}"
