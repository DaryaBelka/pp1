def f(n):
   if n == 1:
      return 0
   elif n ==2 or n == 3:
      return 1
   return f(n-1) + f(n-2)

 