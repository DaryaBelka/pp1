import json

with open("euro.json", "r") as file:
   rates = json.load(file)
   print(rates)

for i in rates["rates"]:
    print("Date", "     ","Buying Rate", "     ","Selling Rate")
    print("=====================================================")
    print(i['effectiveDate'], "   ",i['bid'], "   ",i['ask'])