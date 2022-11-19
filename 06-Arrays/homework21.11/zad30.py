array = [4,2,8,4,7,9,5]
def minmax(array):
   largest = max(array)
   smallest = min(array)
   return [smallest,largest]
print(minmax(array))