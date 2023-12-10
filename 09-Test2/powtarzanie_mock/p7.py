# A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. 
# Create a function f(arr) that, for a given array of usernames, returns the number of valid usernames in the array

# 1 wersja 
# import re
# def f(arr):
#    count = 0
#    a = re.compile(r"^[a-z0-9_]{4,12}$")
#    for i in arr:
#       if a.match(i):
#          count +=1 
#    return count

import re
def f(arr):
   count=0
   for i in arr:
      if 4<= len(i) <=12:
         if re.findall('[a-z0-9]_',i):
            count+=1
   return count
        

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))