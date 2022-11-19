def create_2d_arr(x, y):
    arr = [[0 for j in range(y)] for i in range(x)]
    return arr
print(create_2d_arr(3, 5))