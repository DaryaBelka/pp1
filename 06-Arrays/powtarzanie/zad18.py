arr = [[True,False],[True,True],[False,False]]
print(f"Before: {arr}")

for i in range(len(arr)):
   for j in range(len(arr[i])):
      arr[i][j] = not arr[i][j]
         

print(f"After: {arr}")
