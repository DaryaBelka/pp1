def f(array2D):
   sum = 0
   sum1 = 0
   sum2 = 0
   sum3 = 0
   for i in range(len(array2D)):
      sum += array2D[i][0]
      sum1 += array2D[i][1]
      sum2 += array2D[i][2]
      sum3 += array2D[i][-1]
   return sum, sum1, sum2, sum3
array2D = [3,6,2,7], [9,5,4,0], [2,8,0,9]
print(f(array2D))


