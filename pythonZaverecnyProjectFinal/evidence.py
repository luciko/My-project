from pojistenec import Pojistenec


class Evidence:

    def __init__(self):
        pass

    """Metoda přidá nového pojištěnce dle zadaných parametrů od uživatele"""
    def pridat(self):
        print("\nNíže uveďte údaje nového pojištěnce")
        jmeno = input("* zadejte jméno: ")
        prijmeni = input("* zadejte příjmení: ")
        vek = input("* zadejte věk: ")
        telefon = input("* zadejte telefon: ")
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        return novy_pojistenec

    """Metoda vypíše všechny pojištěnce v evidenci"""
    def vypsat(self, pojistenci):
        print("\nVýpis všech pojištěnců:")
        for i in pojistenci:
            print(i)

    """Metoda vyhledá pojištěnce v evidenci dle parametrů jméno a příjmení zadaných od uživatele.
    V případě, že dané jméno s příjmením se v evidenci nenachází, vypíše hlášení o nenalezení dané osoby."""
    def vyhledat(self, pojistenci):
        print("\nNíže uveďte údaje hledaného pojištěnce")
        zadane_jmeno = input("* zadejte hledané jméno: ")
        zadane_prijmeni = input("* zadejte hledané příjmnení: ")
        print("\nVyhledaný pojištěnec:")
        for i in pojistenci:
            if (zadane_jmeno == i.jmeno) and (zadane_prijmeni == i.prijmeni):
                print(i)
            else:
                print("Hledaný pojištenec nebyl nalezen.")
