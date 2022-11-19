arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
for i in range(len(arr1)):
   if arr1[i] not in arr2:
      print(arr1[i], end = ' ')
