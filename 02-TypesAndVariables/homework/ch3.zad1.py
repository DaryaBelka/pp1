from ast import If


a = int(input("Podaj liczbę godzin:"))
b = int(input("Podaj stawkę godzinową:"))
if a > 40:
     print(f'Wynagrodzenie: {40*b+(a-40)*b*1.5}')
else:
     print(f'Wynagrodzenie: {a*b}')
