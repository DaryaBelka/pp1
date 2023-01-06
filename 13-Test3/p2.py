def f(arr):
   for i in arr:
      if len(arr) == 0 or len(i) != len(arr):
         return False
      elif i[0]+i[0] != i[1]:
         return False
   return True
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
print(f([[1,2],[3,6]]))
          