x = 0
y = 0
z = 0
while y != "gotowe":
    try:
        y = input("Podaj liczbe albo napisz 'gotowe':")
        x = x + int(y)
        z += 1
    except ValueError:
        if y == "gotowe":
            print(x, z, x/z)
        else:
            print("Nieprawidłowe wejście")
            continue