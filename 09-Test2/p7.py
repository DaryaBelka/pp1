import csv
def f(age, gender):
   count = 0 
   with open("test.csv", "r", encoding="UTF-8") as file:
      data = csv.reader(file)
      for i in data:
         a = int(i[3])
         if a == age and i[2] == gender:
            count += 1
   return count
print(f(40,"Female"))
