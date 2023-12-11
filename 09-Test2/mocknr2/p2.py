def f2(a1,a2):
   count1 = 0
   count2 = 0
   for i in a1:
      if 100>i>9:
         count1 +=1
   for j in a2:
      if 100>j>9:
         count2 +=1
   if count1 == count2:
      return True
   return False

print(f2([23,7,16,34],[1,18,79,20,6,111]))