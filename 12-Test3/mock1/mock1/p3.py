def f(uid):
   a = []
   for i in uid:
      if i not in a :
         a.append(i)
         if len(uid)==len(a):
            return True
   return False
   


print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]))

