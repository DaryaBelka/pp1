class C:
  def __init__(self, arr):
    self.arr = arr
  def __str__(self):
    sum = 0
    for num in self.arr:
      sum += num
    return "+".join([str(num) for num in self.arr]) + f"={sum}"

print(C([5,12]))
print(C([6,0,15]))