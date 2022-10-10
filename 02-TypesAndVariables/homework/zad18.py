a = int(input("Side1: "))
b = int(input("Side2: "))
c = int(input("Side3: "))
p =  (a + b + c)/2
area = int((p*(p-a)*(p-b)*(p-c))**(1/2))
print(f'Area is {area}')