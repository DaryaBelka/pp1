try:
    a = float(input("Podaj wartość pomiędzy 0.0 a 1.0:"))
    if a > 0 and a <= 1:
        if a < 0.6:
            print("F")
        elif a >= 0.6 and a < 0.7:
            print("D")
        elif a >= 0.7 and a < 0.8:
            print("C")
        elif a >= 0.8 and a < 0.9:
            print("B")
        elif a >= 0.9:
            print("A")
    else:
        print("Niepoprawna wartość")
except:
    print("Podaj wartość float:")