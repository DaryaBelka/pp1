def f5(c):
   with open("data.txt", "r", encoding="UTF-8") as file:
      count = 0
      for line in file:
         a = line.split()
         for word in a:
            if c in word:
               count += 1
      return count

print(f5("m"))