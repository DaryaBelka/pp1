for i in range(3):
   a = input("Enter the PIN code: ")
   if a == "0805":
      print("Super")
      break
   else: 
      print("Incorrect")
else: 
   print("Sorry, you payment card has been blocked.")
