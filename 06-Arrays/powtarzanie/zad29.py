def f(arr1, arr2):
   count = 0 
   for i in arr1:
      if i not in arr2:
         count +=1
   return count

print(f([4,36,12,28,9,44,5],[5,1,36]))