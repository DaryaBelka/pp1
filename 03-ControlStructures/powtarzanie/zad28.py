a = str(input("Enter EAN-13 article number: "))
if a[0:3] == "590" and len(a) == 13:
   print("Article number is correct","Article manufactured in Poland", sep = "\n")
else:
   print("Error")


