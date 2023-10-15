a = int(input("Enter your height in cm: "))
b = int(input("Enter your weight in kg: "))
num = b/(a/100)**2
print(f"Your BMI index: {round(num, 2)}")
if 18.5<num<25:
   print("Correct weight: True")
else:
   print("Correct weight: False")