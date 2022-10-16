lista = []
x = None
while x != "gotowe":
    try:
        x = int(input("Podaj liczbe albo napisz 'gotowe':"))
        continue
    except ValueError:
        print("Niepoprawna wartość")
        break
print(f'')