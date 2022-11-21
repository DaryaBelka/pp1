f=open('.\\07-FileHandling\\zad19.txt','w')
for i in range(1,50):
    f.write(f'{i}\n')
f.close()
f=open('.\\07-FileHandling\\zad19.txt','r')
print(f.read())
f.close()