def f(binary_number):
   for i in binary_number:
      if i not in "01":
         return False
   return True

print(f("10110"))
print(f("11111"))