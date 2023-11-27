array = [[-38, 19], [5,40],[-7,11],[29,16]]
a = min(array[0])
b = max(array[0])
for i in array:
   min_value = min(i)
   max_value = max(i)

   a = min(a, min_value)
   b = max(b, max_value)
print(a,b)