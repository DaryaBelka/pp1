import math
def f(amount_to_pay):
   a = math.floor(amount_to_pay//5)
   b = amount_to_pay - a*5
   c = math.floor(b//2)
   z = b - c*2
   return a+c+z

print(f())