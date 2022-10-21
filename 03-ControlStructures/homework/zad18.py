import math
from re import X
from this import d
from tkinter import Y


a = int(input("Enter the amount in PLN: "))
x = math.floor(a/5)
y = a - x*5
z = math.floor(y/2)
b = y - z*2
print(f'The amount of PLN {a} in coins: 5zl-{x}, 2zl-{z}, 1zl-{b}')


