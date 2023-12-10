def f(array2D):
   for i in range(len(array2D)):
      row_sum = 0
      col_sum = 0
      for j in range(len(array2D)):
         row_sum += array2D[i][j]
         col_sum += array2D[j][i]
      if row_sum != col_sum:
         return False
   return True


print(f([[3, 7, 2], [4, 2, 5], [5, 2, 1]]))  
print(f([[3, 7, 2], [4, 2, 5], [9, 2, 1]]))
