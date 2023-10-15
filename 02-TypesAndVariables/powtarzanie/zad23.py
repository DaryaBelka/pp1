a,b,c = float(input("Enter a: ")), float(input("Enter b: ")), float(input("Enter c: "))
p = (1/2)*(a+b+c)
print(f"Triangle area: {(p*(p-a)*(p-b)*(p-c))**(1/2)}")
print(f"Triangle circumference: {a+b+c}")