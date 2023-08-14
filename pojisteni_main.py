from pojisteni_pojistenec import pojistenec

pojistenci = []
volba = 0

print("///////*EVIDENCE POJISTENI*///////")
print("\\\\\\\\\\\\\\*EVIDENCE POJISTENI*\\\\\\\\\\\\\\")
print("///////*EVIDENCE POJISTENI*///////")

# vypsání možností pro volbu uživatelem
while volba != 4:
    print("\n-----ZVOLTE ČÍSLO Z MOŽNOSTÍ-----")
    print("1 -> Vložit nového pojištěnce")
    print("2 -> Vypsat všechny pojištěnce")
    print("3 -> Hledání pojištěnce")
    print("4 -> Konec\n")

    # kontrola, jestli je volba správně zadána uživatelem
    try:
        volba = int(input())
    except ValueError:
        print("Zadaná hodnota není číslo. Prosím zadejte znovu.\n")
        continue

    # kód pro provedení jednotlivých možností
    match volba:
        case 1:
            print("ZVOLILI JSTE 'ZADAT NOVÉHO POJIŠTĚNCE'")
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            while True:
                try:
                    vek = int(input("Zadejte věk: "))
                    break
                except ValueError:
                    print("\nZadaná hodnota není číslo. Prosím zadejte znovu.\n")
            telefon = input("Zadejte telefonní číslo: ")

            pojistenci.append(pojistenec(jmeno, prijmeni, vek, telefon))
            print("\nVložení pojištěnce proběhlo v pořádku.\n")

        case 2:
            if len(pojistenci) > 0:
                print("JMÉNO\tPŘÍJMENÍ\tVĚK\tTELEFON")
                for osoba in pojistenci:
                    print(osoba)
            else:
                print("\nV seznamu pojištěnců ještě nikdo není.\n")

        case 3:
            if len(pojistenci) > 0:
                jmeno_pojistence = input("Zadejte jméno hledaného pojištěnce: ")
                prijmeni_pojistence = input("Zadejte příjmení hledaného pojištěnce: ")
                pojistenec_nalezen = 0
                for osoba in pojistenci:
                    if osoba.jmeno == jmeno_pojistence and osoba.prijmeni == prijmeni_pojistence:
                        print("JMÉNO\tPŘÍJMENÍ\tVĚK\tTELEFON")
                        print(osoba)
                        pojistenec_nalezen = 1
                        break
                if pojistenec_nalezen == 0:
                    print("\nPojištěnec nenalezen.\n")
            else:
                print("\nV seznamu pojištěnců ještě nikdo není.\n")

        case 4:
            continue

        case _:
            print("\nTomuto číslu neodpovídá žádná z možností, zadejte číslo znovu.\n")
            continue
