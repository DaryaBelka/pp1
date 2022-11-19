array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
minimum = 0
maximum = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < minimum:
            minimum = array[i][j]
            indminr = i
            indminc = j
        elif array[i][j] > maximum:
            maximum = array[i][j]
            indmaxr = i
            indmaxc = j
print("Smallest value: ", minimum, '(row:', indminr, ',', 'column: ', indminc, ')')
print("Largest value: ", maximum, '(row: ', indmaxr, ',', 'column: ', indmaxc, ')')
