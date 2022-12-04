def f(first_letter,last_letter):
   with open("test.txt", "r", encoding="UTF-8") as file:
      licznik = 0
      for line in file:
         words_in_line = line.split()
         for word in words_in_line:
            if first_letter == word[0] and last_letter == word[-1]:
               licznik += 1
      return licznik
print(f("w","d"))
