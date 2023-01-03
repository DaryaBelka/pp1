def f(d):
   in_car_park = {}
   for i in d:
      registration, action = i[0], i[1]
      if action == "in":
            in_car_park[registration] = True
      elif action == "out":
         if registration in in_car_park:
            del in_car_park[registration]
   return sorted(in_car_park.keys())

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))