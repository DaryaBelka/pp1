import random 
def generate_number():
   b = int(input("Enter a number 1-9 : "))
   a = random.randint(1,9)
   if a == b:
      return("You won the game!!")
   return("Haha")
   
print(generate_number())

