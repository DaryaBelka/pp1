x = 0
y = 0
z = 0
while x != "gotowe":
    try:
        x = input("Podaj liczbe albo napisz 'gotowe':")
        y = y + int(x)
        z += 1
    except ValueError:
        if x == "gotowe":
            print(y, z, y/z)
        else:
            print("Niepoprawna wartość")