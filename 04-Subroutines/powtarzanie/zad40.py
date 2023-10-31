def f(number):
   sum = 0 
   a = set()
   num_str = str(number)
   for i in num_str:
      if num_str.count(i) > 1:
         a.add(i)
         sum += int(i)
   return sum

print(f(513553007))