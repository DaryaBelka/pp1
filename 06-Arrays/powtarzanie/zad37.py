def second_largest(arr):
   sort_arr = sorted(arr)
   return sort_arr[-2]

def diff(arr):
   max_num = max(arr)
   min_num = min(arr)
   return max_num-min_num

def median(arr):
   sort_arr = sorted(arr)
   a = len(sort_arr)//2
   if len(sort_arr)%2==0:
      return (sort_arr[a-1]+sort_arr[a])/2
   else:
      return arr[a]


def smlar(arr):
   max_num = max(arr)
   min_num = min(arr)
   return min_num, max_num

def separmin(arr):
   return "-".join(map(str, arr))

