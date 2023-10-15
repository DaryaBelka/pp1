a = input("Enter credit card number: ")
if len(a)==16:
   print(f"Card number: {a[0:4]} {a[4:8]} {a[8:12]} {a[12:16]}")