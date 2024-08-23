def diagonal_difference(arr):
    length = len(arr[0])
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(length):
            primary_diagonal+=arr[i][i]
            secondary_diagonal += arr[i][length-1-i]
    return abs(primary_diagonal-secondary_diagonal)
arr = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]

print(diagonal_difference(arr))
