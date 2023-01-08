class C:
   def m1(n):
      result = ''
      for digit in str(n):
         if digit in '2468':
            result+=digit
      return result

   def m2(n):
      n_str = str(n)
      a = n_str[0]
      for i in n_str[1:]:
         if i < a:
            return False
      return True
   
   def m3(n):
      n_str = str(n)
      n_digits = set(n_str)
      m3 = "".join([str(i) for i in range(10) if str(i) not in n_digits])
      return m3

print(C.m1(4231564))
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))

         


     
