import random

for i in range(40):
   print("-", end = '' )
print()
arr = []
for j in range(8):
   ar= random.randint(1,1000)
   arr.append(ar)

print("|", end='')
for l in arr:
   print(f' {l}|', end = "")
   
print()

for i in range(40):
   print("-", end = '' )
print()
