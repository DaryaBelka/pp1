array = [2,3,2,5,8,1,9,8]
result = []
for i in range(len(array)): 
   for j in range(len(array)):
      if i != j and array[i] == array[j]:
         array[j], array[i] = 0, 0
for i in array:
   if i != 0:
      print(i, end = ' ')
   