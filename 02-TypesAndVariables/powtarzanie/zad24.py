a = input("Enter vehicle registration number: ")
if ("KR" in a[0:2] or "KK" in a[0:2]) and len(a)==7:
   print(f"Car from Kraków: True")
else:
   print(f"Car from Kraków: False")