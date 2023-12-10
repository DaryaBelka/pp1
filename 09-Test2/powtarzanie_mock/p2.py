def f(arr):
   b = []
   for i in arr:
      if arr.count(i) == 1:
         b.append(i)
   for i1 in b:
      return i1
print(f([7,7,7,7,7,5,7,7]))
