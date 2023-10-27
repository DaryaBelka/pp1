def numbers(n): 
   a = [ ]
   for i in range(1, n+1):
      a.append(str(i))
   return " ".join(a)
   
print(numbers(15))