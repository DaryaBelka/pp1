for i in range(1,4):
    a=input("Enter the PIN code: ")
    if a=="0805":
        print('Your PIN code is correct', end = '')
    else:
        if i<3:
            print("Incorrect...")
        if i==3:
            print("Sorry,your payment card has been blocked")
    