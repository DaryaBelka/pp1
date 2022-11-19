array = [1.0, 30.5, 45.3, 5.2, 7.0, 56.0]
value = float(input("Enter the value: "))
a = 0
for i in array:
    if value < i:
        a += 1
print(a)