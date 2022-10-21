for i in range(1,31):
    if i%3 == 0:
        if i%5 == 0:
            print('BINGO', end=" ")
        else: 
            print('THREE', end=" ")
    elif i%5 == 0:
        print('FIVE', end=" ")   
    else:
        print(i, end=" ")
