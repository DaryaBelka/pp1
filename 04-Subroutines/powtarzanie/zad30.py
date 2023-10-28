def f(number, even):
   sum = 0
   for i in str(number):
      if (even and int(i)%2==0) or (not even and int(i)%2==1):
         sum += int(i)
   return sum

print(f(13115, True))
