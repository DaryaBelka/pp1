def f(palindrome):
   a = palindrome[::-1]
   if a == palindrome:
      return True
   return False

print(f("12-11-22"))