def month(n): 
   a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   return (f"The name of month {n} is {a[n-1]}")

print(month(6))