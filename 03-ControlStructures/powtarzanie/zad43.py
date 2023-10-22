def fib(n):
   sum = 0
   a = 0
   b = 1
   for i in range(n-1):
      a, b = b, a + b
      sum += a
   return sum

print(fib(7))