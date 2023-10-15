import random 
a = random.randint(1,6)
print(f"Dice rolled: {a}")
if a == 6 or a == 1:
   print("Special number: True")
else:
   print("Special number: False")