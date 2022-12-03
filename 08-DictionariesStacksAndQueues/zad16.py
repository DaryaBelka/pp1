import json
with open("students.json", "r") as file:
   students = json.load(file)

with open("limited.json", "w") as j:
   for i in students:
      j.write(i["name"])
      j.write(" ")
      j.write(i["surname"])
      j.write(" ")
      j.write((str(i["student ID"])))
      j.write("\n")
