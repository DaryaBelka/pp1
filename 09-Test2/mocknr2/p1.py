def f1(a):
   count = 0
   for i in a:
      if i>8 and i%2==0:
         count +=1
   return count
print(f1([13,7,4,16,3,12,8]))