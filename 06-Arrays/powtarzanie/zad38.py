arr = [3,4,5,6,7,8,2]
a = int(input("Enter number: "))

count = 0
for i in arr:
   if a < i:
      count += 1

print(count)