a = str(input("Enter phone number: "))
if len(a)==9:
   print(f"Phone number: {a[0:3]}-{a[3:6]}-{a[6:9]}")
else:
   print("Error")