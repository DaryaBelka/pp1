def f1(t):
   import re
   names = re.findall(r"[A-Z][a-z]+",t)
   ages = re.findall(r"\d+",t)
   result = {}
   for i in range(len(names)):
      result[names[i]] = ages[i] 
   return dict(sorted(result.items()))

print(f1("Mark is 24 and Ann is 27"))
print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))




