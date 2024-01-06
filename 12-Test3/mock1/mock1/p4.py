def f(fnc,prods):
   a = []
   for i in prods: 
      a.append(fnc(i))
   return ",".join(a)



prods = ["water","cheese","tomato"] 
fnc1 = lambda x: "id:"+x[:2]
print(f(fnc1,prods))
prods = ["water","cheese","tomato"] 
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc2,prods))
