def f(x,y):
   count = []
   for i in range(x,y):
      if i<0 and i%2==0:
         count.append(i)

   return len(count) 

print(f(-7,8)) 