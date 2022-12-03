import json
with open("\\.08-DictionariesStacksAndQueues\\students.json", "r") as file:
   students = json.load(file)

with open("limited.json", "w"):
   for i in students:
      j.write(i[name])
      j.wtite(" ")
      j.write(i[surname])
      j.wtite(" ")
      j.write((i[ID]))
      j.wtite(" ")
