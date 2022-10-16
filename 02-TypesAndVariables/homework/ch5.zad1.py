x, y, z = 0, 0, 0
while x != 'gotowe':
    try:
        x = int(input('Podaj liczbe albo napisz 'gotowe':'))
        y = y + x
        z += 1
    except ValueError:
        if x == 'gotowe':
            print(y, z, y/z)
        else:
            print('Niepoprawna wartość')