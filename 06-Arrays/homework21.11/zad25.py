number = int(input("Number: "))
print("Array:", end = " ")
array = [int(i) for i in input().split()]
def occurs(number, array):
   if number in array:
      return True
   return False
print("Result: ", occurs(number, array))

