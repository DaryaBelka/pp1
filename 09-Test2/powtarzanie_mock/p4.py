def f(subjects):
   max_average = 0
   subject_new = ""

   for key, value in subjects.items():
      a = sum(value)/ len(value)
      if a> max_average:
         max_average = a
         subject_new = key
   return subject_new

      

print(f({"math":[4,4],"geo":[5,4,4,4],"comp":[5,4]}))
