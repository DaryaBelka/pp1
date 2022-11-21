a = input('File name: ')
file = open('.\\07-FileHandling\\countries.txt','r') 
licznik = 1
for line in file:
   print(f'Number of lines: {licznik}')
   licznik += 1 
file.close()