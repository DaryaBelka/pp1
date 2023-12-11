import re
def f3(t):
   sum = 0
   a = re.findall(r'\b\d{2}\b', t)
   b = re.findall(r'\b\d{3}\b', t)
   for i in a:
      sum += int(i)
   for i1 in b:
      sum += int(i1)
   return sum

print(f3("Przykladowe liczby parzyste to 16, 2, 114 oraz 1014, a takze 8"))

