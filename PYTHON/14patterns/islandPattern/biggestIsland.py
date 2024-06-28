class solution:
    def biggestIsland(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        biggestIslandArea = 0  # Initialize biggestIslandArea

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    biggestIslandArea = max(biggestIslandArea, self.dfs(matrix, i, j))

        return biggestIslandArea

    def dfs(self, matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0
        if matrix[i][j] == 0:
            return 0

        matrix[i][j] = 0

        area = 1

        area += self.dfs(matrix, i + 1, j)
        area += self.dfs(matrix, i - 1, j)
        area += self.dfs(matrix, i, j + 1)
        area += self.dfs(matrix, i, j - 1)

        return area

def main():
    sol = solution()
    print(sol.biggestIsland([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()
