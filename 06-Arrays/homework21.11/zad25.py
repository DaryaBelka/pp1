'''number = input('enter number: ')
array = input('enter array: ')
def occurs(number, array):
   for i in range(len(array)):
      if i==number:
         print('number {number} appears in the array')
      else:
         print('number {number} dont appears in the array')
result = occurs(number, array)
print(result)'''

number = int(input("Number: "))
print("Array:", end = " ")
array = [int(i) for i in input().split()]
def occurs(number, array):
   if number in array:
      return True
   return False
print("Result: ", occurs(number, array))

