while True:
    try:
        e = float(input("Eerste getal? "))
        break
    except ValueError:
        print("Fout: Dit is geen geldig getal!")

while True:
    try:
        t = float(input("Tweede getal? "))
        break
    except ValueError:
        print("Fout: Dit is geen geldig getal!")

e = float(e)
t = float(t)

print("Sum = ", e + t ,"Min = ", e - t , "Ver = ", e * t , "Del = ", e / t)