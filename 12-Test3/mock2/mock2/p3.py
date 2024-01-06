def f(d):
   sum = 0
   count = 0
   for key, value in d.items():
         sum += int(value)
         if sum/len(d) < value:
            count +=1
   return count


print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))