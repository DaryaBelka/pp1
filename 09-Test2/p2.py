def f(human_age):
   if human_age == 0:
      print('error')
   elif human_age<=2:
      a = human_age*10
      return a
   elif human_age>2:
      b = 2*10+(human_age-2)*4
      return b
   else:
      pass
print(f(15))
print(f(2))



