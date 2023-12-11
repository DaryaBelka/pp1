def f4(d):
   max_sum = 0
   for key, value in d.items():
      for i in value:
         if 4<i<11:
            max_sum += i
   return max_sum


print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))
