arr = [3,4,5,7,6,7,3]
arr1 = []
arr2 = []
for i in arr:
   if i%2==0:
      arr1.append(i)
   else:
      arr2.append(i)

print(arr1 + arr2)