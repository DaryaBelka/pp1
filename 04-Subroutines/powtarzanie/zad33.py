def f(n):
   if n == 0:
      return ""
   elif n>0:
      return "*" + "/*"*(n-1)
   
print(f(4))