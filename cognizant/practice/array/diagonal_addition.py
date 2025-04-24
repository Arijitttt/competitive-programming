matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
primary_diagonal = 0
secondary_diagonal = 0
for i in range(len(matrix)):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][len(matrix)-1-i]
print(abs(primary_diagonal-secondary_diagonal))