def number(x,y):
   a = int(input("A number: "))
   if a in range(x,y):
      return "yes"
   return "no"

print(number(2,15))