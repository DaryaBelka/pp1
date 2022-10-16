x, y, z = 0
while y != "done":
    try:
        y = int(input(" Podaj liczbe albo napisz 'gotowe' :"))
    except:
        if y == "done":
            print(x, z, x/z)
        else:
            print("Niepoprawna wartość")