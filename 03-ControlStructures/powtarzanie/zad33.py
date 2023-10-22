def f(number):
   b = ""
   while number > 0:
      a = number % 2
      b = str(a) + b
      number = number // 2
   return b
print(f(12))