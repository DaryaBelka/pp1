arr = [[1,3,5],[8,7,2]]
print(arr[0][0]+arr[-1][-1])

middle = len(arr[0])//2
print(arr[0][middle]+arr[-1][middle])

sum = 0
for i in arr[-1]:
   sum += i
print(sum)
