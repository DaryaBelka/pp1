phone = {
    "brand": "Xiaomi",
    "model": "Redmi Note 6 Pro",
    "age": 4,
    "RAM": '4GB',
    "broken": False,
    "phone numbers in SIM cards":{"Belarusian":"+375293539656","Polish":"+48573399759"}
   }

#for key in phone.keys():
#   value = phone[key]
#   print(key, '=', value)

for k,v in phone.items():
    print(k,'=',v)