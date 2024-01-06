def f(x,y,d):
   for i in range(x,y+1):
      a = str(i).count(str(d))
      if a >0:
         return True
   return False

print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,210,"04"))