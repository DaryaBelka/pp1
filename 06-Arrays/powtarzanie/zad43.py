def f(text):
   return text

def f1(text):
   a = text.split()
   return len(a)

def f2(text):
   a = text.split()
   return ",".join(sorted(a, key = len, reverse=True))

def f3(text):
   a = text.split()

   return ",".join(sorted(a, key=lambda x: x.lower()))

print(f3("An apple a day keeps the doctor away"))