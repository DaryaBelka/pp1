from ast import If


a = int(input("Podaj liczbę godzin:"))
b = int(input("Podaj stawkę godzinową:"))
if a.isnumeric() == False:
     print('error')
elif b.isnumeric() == False:
     print('error')
else:
     if a > 40 :
          print(f'Wynagrodzenie: {40*b+(a-40)*b*1.5}')
     else :
          print(f'Wynagrodzenie: {a*b}')
