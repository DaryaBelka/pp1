def f(n):
   if n<=0:
      return ""
   elif n>1 and n<=5:
      i = ""
      i += "/" * n
      return i
   elif n>5:
      a = n//5
      b = n%5
      c = ("/////-")*a + "" + "/"*b
      return c


