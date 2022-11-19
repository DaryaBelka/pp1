print("Enter the array: ")
array = [int(i) for i in input().split()]
n = len(array)
print(array)
sum = 0
a = 0
while a <= n - 1:
    sum += array[a]
    a += 1
print(sum/n)
