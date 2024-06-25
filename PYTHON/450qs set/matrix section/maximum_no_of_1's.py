# matrix = [
#     [1, 0, 1],
#     [1, 1, 1],
#     [0, 0, 1]

# ]
# temp = []
# rows = len(matrix)
# columns = len(matrix[0])
# for i in range(len(matrix)):
#     # for j in range(len(matrix[i])):

#     temp.append(matrix[i])

# z=max(temp)
# print(z)


def maximum_no_of_one(matrix):
    temp = []
    for i in range(len(matrix)):

        temp.append(matrix[i])
    for j in range(len(temp)):
        if temp[j]==max(temp):
            return j
matrix = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]

]
print(maximum_no_of_one(matrix))