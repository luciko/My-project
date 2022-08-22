from evidence import Evidence

evidence = Evidence()
pojistenci = []

pokracovat = True
while pokracovat:
    print("-----------------------------\n"+"EVIDENCE POJIŠTĚNÝCH\n"+"-----------------------------\n")
    print("Jakou akci si přejete provést:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec\n")
    print("Vaše volba je: ", end="")
    volba = int(input())
    if volba == 1:
        novy_zaznam = evidence.pridat()
        pojistenci.append(novy_zaznam)
        print("\nData byla uložena do evidence. Zpět na menu s výběrem akce pokračujte klávesou Enter...")
        input()
    elif volba == 2:
        evidence.vypsat(pojistenci)
        print("\nZpět na menu s výběrem akce pokračujte klávesou Enter...")
        input()
    elif volba == 3:
        evidence.vyhledat(pojistenci)
        print("\nZpět na menu s výběrem akce pokračujte klávesou Enter...")
        input()
    else:
        print("Děkujeme za použití Evidence pojištěných. Nashledanou.")
        pokracovat = False
