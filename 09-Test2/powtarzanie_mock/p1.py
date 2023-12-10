def f(player1,player2):
   card = {
      "A":10,
      "K":10,
      "Q":10,
      "J":10,
      "T":10,
      "9":9,
      "8":8,
      "7":7,
      "6":6,
      "5":5,
      "4":4,
      "3":3,
      "2":2,
      "1":1
   }
   sum1 = 0
   for i1 in player1:
      sum1 += card[i1]
   
   sum2 = 0
   for i2 in player2:
      sum2+= card[i2]

   if sum1>sum2:
      return True
   return False
   
print(f("9532", "K8"))
