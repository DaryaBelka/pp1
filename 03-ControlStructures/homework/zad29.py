from re import X


x = 0
y = 0
z = 0
while True:
    a = int(input("Enter number: "))
    if a == 0:
        print(f'RESULT: Quantity={y}, Sum={x}, Mean={z}')
        break
    else:
        x = x + a
        y = y + 1
        z = int(x/y)