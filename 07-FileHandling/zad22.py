file = open('.\\07-FileHandling\\students.txt','r')
for i in file:
   for j in i:
      if j[3]<30:
         print(j[1][2][5])

a = file.read()
print(a)
file.close()
