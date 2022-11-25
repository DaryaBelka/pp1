file=open('.\\07-FileHandling\\zad15.txt','r')
file1=open('.\\07-FileHandling\\copylines.txt','w')
for line in file:
   file1.write(f'{line}')
file.close()
file1.close()