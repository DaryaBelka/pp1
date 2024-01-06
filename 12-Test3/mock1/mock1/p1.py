def f(word):
   a = []
   for i in range(len(word)):
      b = word[i].lower() + word[i].capitalize() + word[i+1:].lower()
      a.append(b)
   return "-".join(a)


print(f("book"))
print(f("water"))
print(f("ok"))
print(f("a"))
print(f(""))