a = 4
b = 15
for x in range(a):
    for y in range(b):
        if(x==0 or y==0 or x== a-1 or y== b-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print( )