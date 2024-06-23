def search(matrix, rows, cols, key):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == key:
                return True
    return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
rows = len(matrix)
cols = len(matrix[0])
key = 11

if search(matrix, rows, cols, key):
    print('Key found')
else:
    print('Key not found')
