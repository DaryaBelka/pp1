def f(arr):
    rows = len(arr)
    columns = len(arr[0])
    for i in range(rows):
        for j in range(columns):
            if arr[i][j]!=(i+1)*(j+1):
                return False
    return True

print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[2,4]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,4,6]]))
print(f([[1,2,3],[2,5,6]]))
          