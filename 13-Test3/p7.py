class C:
   def __init__(self, num):
      self.num = num
   def m1(self):
      for i in self.num:
         n = i%2
         if n==0:
            return n
   def m2(self):
      for i in self.num:
         if i<=i[:1]:
            return True
         else:
            return False


print(C.m1(4231564))
         


     
