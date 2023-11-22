arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

long = arr[0]
for i in arr:
   if len(i) > len(long):
      long = i

print(long)
