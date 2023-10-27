def numbers(n): 
   a = [ ]
   for i in range(1, n+1):
      a.append(i)
   return " ".join(a)
   
print(numbers(15))