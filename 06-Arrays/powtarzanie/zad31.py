array = [2,3,2,5,8,1,9,8]

arr1 = []

for i in array:
   if array.count(i)>1:
      arr1.append(i)

for j in arr1:
   if j in array:
      array.remove(j)
print(" ".join(map(str, array)))