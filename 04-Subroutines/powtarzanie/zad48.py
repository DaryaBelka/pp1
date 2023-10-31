def f(product_code):
   a = product_code[0:3]
   sum = 0
   for i in a:
      sum += int(i)
   if sum%7 == int(product_code[-1]):
      return True
   return False


print(f("7071"))