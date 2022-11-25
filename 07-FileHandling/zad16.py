import shutil
file=open('.\\07-FileHandling\\copy.txt','w')
a = shutil.copy('\\07-FileHandling\\zad15.txt', 'r')
file.write(a)
file.close
file=open('.\\07-FileHandling\\copy.txt','r')
print(file.read())
file.close()