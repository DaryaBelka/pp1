import random
a=random.randint(100,999)
f=open('.\\07-FileHandling\\zad20.txt','w')
for i in range(50):
    f.write(f'{random.randint(100,999)}\n')
f.close
f=open('.\\07-FileHandling\\zad20.txt','r')
print(f.read())
f.close()