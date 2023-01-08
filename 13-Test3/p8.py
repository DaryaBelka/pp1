class C:
   def __init__(self, d):
      self.d = d
        
   def m(self, n):
      result = []
      names = ""
      for key in self.d:
         grades_average = sum(self.d[key])/len(self.d[key])
         if grades_average >= n:
            result.append(key)
      result = sorted(result)
      for name in result:
         names+=name+","
      return names[:-1]
        
s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(4))
print(s.m(3))
print(s.m(5))