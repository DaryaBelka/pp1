import csv
def f(gender):
   count = 0 
   with open("test.csv", "r", encoding="UTF-8") as file:
      data = csv.reader(file)
      for i in data:
         if i[3] == gender:
            count += 1
   return count
print(f("Female"))
