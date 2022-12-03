def f(first_letter,last_letter):
   licznik = 0
   with open("test1.txt", "r") as file:
      for line in file:
         words_in_line = line.split()
         for word in words_in_line:
            if first_letter == word[0] and last_letter == word[-1]:
               licznik += 1
   return licznik
print(f("w","d"))
print(f("u","d"))