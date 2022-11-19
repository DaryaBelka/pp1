arr = [2,8,5,3,6]
def bubblesort(arr):
   n = len(arr)
   for i in range(n-1):
      for j in range(0, n-1-i):
         if (arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j],arr[j+1]
            return bubblesort(arr)
         else:
            pass
print(bubblesort(arr))
