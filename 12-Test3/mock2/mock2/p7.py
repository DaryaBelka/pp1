def f(d): 
   a = []
   for number, register in d:
      if register == "in":
         a.append(number)
      elif register == "out":
         a.remove(number)
   return sorted(a)

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))
cars1 = [["KR234","in"],["KR234","out"]]
print(f(f(cars1)))
