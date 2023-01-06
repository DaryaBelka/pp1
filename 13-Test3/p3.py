def f1(t):
   import re
   a = re.findall(r'(\w+)', t)
   for i in a:
      print(i)
   



def f2(d):
   import re
   a = re.findall(r'\d+', d)
   sum = 0
   for i in a:
      i = int(i)
      sum += i  
   return sum
print(f1("Mark is 24 and Ann is 27"))
print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))   
print(f2("Mark is 24 and Ann is 27"))
print(f2("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))