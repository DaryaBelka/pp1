a = str(input("Enter time (24-hour format): "))
b = a.split(":")
if 24>=int(b[0])>=12 and int(b[1])<=60:
   print(f"Time in 12-hour format: {int(b[0])-12}:{a[3:5]}")
elif int(b[1])>=60 or int(b[0])>24:
   print("Error")
else:
   print(f"Time in 12-hour format: {a}")
