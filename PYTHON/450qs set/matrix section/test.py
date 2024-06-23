matrix  = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#another matrix
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(len(matrix))
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j],end=' ')
#     print()
for i in range(len(matrix)):
    for j in  range(len(matrix)):
        print(matrix[i][j]+matrix2[i][j],end=' ')
    print()
