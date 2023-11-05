import math
def f(amount_pay):
   a = math.floor(amount_pay//5)
   b = amount_pay- a*5
   c = math.floor(b//2)
   d = b - c*2
   return a+c+d

print(f(23))
print(f(8))