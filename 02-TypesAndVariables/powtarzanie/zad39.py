a = float(input("Enter price: "))
b = int(input("Enter discount "))
print(f"Price with discount: {round((a-(a*b/100)),2)}")
print(f"Reduction: {round((a*b/100),2)}")