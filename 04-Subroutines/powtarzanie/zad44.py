def f(password): 
   a = set()
   for i in password:
      if password.count(i) > 1:
         a.add(i)
   if len(set(password)) - len(a)>=6:
      return True
   return False


