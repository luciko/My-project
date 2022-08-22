class Pojistenec:
    """Třída reprezentuje člověka - pojištěnce, který má jméno, příjmení, věk a telefon"""
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} \t {self.prijmeni} \t {self.vek} \t {self.telefon}"
