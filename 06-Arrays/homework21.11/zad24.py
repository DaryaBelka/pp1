array = [2,3,2,5,8,1,9,8]
result = []
for i in range(len(array)): 
   for j in range(len(array)):
      if i != j and array[i] == array[j]:
         print(array[i])
      else:
         pass
print(result)

   
   