arr1 = [9,4,5,8,10]
arr2 = [1,2,3]

print('Orignal list:' + str(arr1))
print('Orignal sub list:' + str(arr2))

flag = 0 
if(all(x in arr1 for x in arr2)):
   flag = 1

if (flag):
      print('The first array is a subset of the second one')
else:
      print('The first array is not a subset of the second one')

