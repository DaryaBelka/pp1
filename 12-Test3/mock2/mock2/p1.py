def f(n):
   a = []
   for i in str(n):
      if int(i)%2==1:
         a.append(i)
   if len(a)==0:
      return -1
   return int(max(a)) - int(min(a))
