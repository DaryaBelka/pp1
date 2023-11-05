def f(name):
   b = name.split()
   a = ""
   for i in b:
      a += i[0]
   return a

print(f("Internet of Things"))
