while True:
    karakter = input("Kies een karakter (Xuy, Zalupa, Debil)\n")
    if karakter == 'Xuy':
        print("Karakter heeft 150 Health en 20 Armour")
        break
    elif karakter == 'Zalupa':
        print("Karakter heeft 30 Health en 100 Armour")
        break
    elif karakter == 'Debil':
        print("Karakter heeft 0 Health en 0 Armour")
        break
    else:
        print(karakter, "is niet toegestaan. Probeer opnieuw.")
