if __name__ == '__main__':
    import random

    losowe = set()

    # Wybór miejsc
    while len(losowe) < 20:
        losowe.add((random.randint(0, 9), random.randint(0, 9)))

    print(losowe)

    # Ustawianie miejsc
    plansza = []
    for i in range(10):
        row = []
        for j in range(10):
            if losowe & {(i, j)}:
                row.append(True)
            else:
                row.append(False)
        plansza.append(row)
    print(plansza)

    # Gra
    strzal = set()
    while losowe:
        x = int(input("Podaj współrzędną x: "))
        y = int(input("Podaj współrzędną y: "))
        if {(x, y)} & strzal:
            print("Juz tu strzelałeś! ")
            continue
        strzal.add((x, y))
        if {(x, y)} & losowe:
            print("Trafiłeś!")
            losowe = losowe - {(x, y)}
        else:
            print("Nie trafiłeś. Próbuj dalej")

    print("Udało Ci się trafić wszystko. Gratulacje")
    print("Ilość twoich prób to: ", len(strzal))

