import json
def f(age, course, average):
   with open("test.json", "r") as file:
      licznik = 0
      for line in file:
         students_line = line.split()
         for student in students_line:
            if age in student and course in student and average in student:
               licznik += 1
      return licznik
print(f(21, "statistics", 4))
