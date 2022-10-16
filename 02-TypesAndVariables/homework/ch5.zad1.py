lista = []
x = None
while x != "gotowe":
    try:
        x = int(input("Podaj liczbe albo napisz 'gotowe':"))
        continue
    except ValueError:
        print("Niepoprawna wartość")
        break
x = sum(lista)
y = len(lista)
srednia = round((x/y), 2)
print(f'Suma: {x}', 'wprowadzono {y} liczb, srednia to {srednia}' )