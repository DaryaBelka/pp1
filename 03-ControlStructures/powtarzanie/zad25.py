a = int(input("Number of products purchased: "))
b = int(input("Product price: "))
if a>2:
   print(f"Amount to pay {(a*b - (a-2)*b*0.25):.2f}")
elif 0<a<3:
   print(f"Amount to pay {(a*b):.2f}")
else:
   print("Error")
