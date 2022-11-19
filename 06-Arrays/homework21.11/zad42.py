array = [[1,2,3,4,5],[1,3,5,7,9],[2,4,6,8,10]]
for i in range(len(array)):
   for j in range(len(array[i])):
      print(array[i][j], end = ' ')
   print()
for i in reversed(array):
   print(*i)


