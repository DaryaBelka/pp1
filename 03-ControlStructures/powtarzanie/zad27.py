facebook = True
twitter = False
instagram = True
if (facebook and twitter) or(facebook and instagram) or (twitter and instagram) or (instagram and twitter and facebook):
   print("A person can be a good influencer!")
else:
   print("Error")