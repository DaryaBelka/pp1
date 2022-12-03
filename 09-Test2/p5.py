def f(first_letter,last_letter):
   licznik = 0
   with open("test.txt", "r") as file:
      for i in file:
         for j in i:
            if first_letter == j[0] and last_letter == j[-1]:
               licznik += j
               return licznik
print(f("w","d"))