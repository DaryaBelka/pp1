file = open('.\\07-FileHandling\\zad15.txt','r') 
file_content = file.read() 
licznik = 0 
for line in file:
   print(f'{licznik}')
print( file_content ) 
file.close()