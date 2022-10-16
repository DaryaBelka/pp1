a = input("Podaj liczbę godzin:")
b = input("Podaj stawkę godzinową:")
if a.isnumeric() == False:
     print('error')
elif b.isnumeric() == False:
     print('error')
else:
    if int(a) > 40 :
     print(f'Wynagrodzenie: {40*int(b)+((int(a)-40))*int(b)*1.5}')
    else :
     print(f'Wynagrodzenie: {int(a)*int(b)}')
