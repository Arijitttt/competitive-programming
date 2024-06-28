def count_islands(matrix):
    def visit_is_land_DFS(matrix, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return  # return, if it is not a valid cell
        if matrix[x][y] == 0:
            return  # return, if it is a water cell

        matrix[x][y] = 0  # mark the cell visited by making it a water cell

        # recursively visit all neighboring cells (horizontally & vertically)
        visit_is_land_DFS(matrix, x + 1, y)  # lower cell
        visit_is_land_DFS(matrix, x - 1, y)  # upper cell
        visit_is_land_DFS(matrix, x, y + 1)  # right cell
        visit_is_land_DFS(matrix, x, y - 1)  # left cell

    rows = len(matrix)
    cols = len(matrix[0])
    total_islands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # only if the cell is a land
                # we have found an island
                total_islands += 1
                visit_is_land_DFS(matrix, i, j)
    return total_islands

def main():
    print(count_islands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(count_islands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()
