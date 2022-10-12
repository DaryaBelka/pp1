from random import randrange


a = randrange(1,7)
b = int(input("Zgadnij od 1 do 6: "))
if b == a:
    print("True")
else:
    print("False")