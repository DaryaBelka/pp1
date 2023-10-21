a = float(input("Current product price: "))
b = float(input("Previous product price: "))
c = 100 - (a/b*100)
if c>=10:
   print("Buy the product!!", f"Product price reduced by {int(c)}%", sep = "\n")
else:
   print("Error")