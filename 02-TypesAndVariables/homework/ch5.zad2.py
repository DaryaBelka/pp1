x = 0
y = 0
z = 1
while y != "gotowe":
    try:
        y = input("Podaj liczbe albo napisz 'gotowe':")
        if int(x) < int(y):
            x = y
        if int(z) > int(y):
            z = y
    except ValueError:
        if y == "gotowe":
            print(f"najwieksza liczba to {x} a najmniejsza to {z}")
        else:
            print("Nieprawidłowe wejście")
            continue