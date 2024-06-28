class solution:
    def countIsland(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        totalIsland = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    totalIsland+=1
                    self.traversing(matrix,i,j)
        return totalIsland
    def traversing(self,matrix,i,j):
        if(i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0])):
            return
        if matrix[i][j] == 0:
            return
        
        matrix[i][j] = 0

        self.traversing(matrix,i+1,j)
        self.traversing(matrix,i-1,j)
        self.traversing(matrix,i,j+1)
        self.traversing(matrix,i,j-1)

def main():
    sol = solution()

    matrix = [[0, 1, 1, 1, 0],
               [0, 0, 0, 1, 1],
                 [0, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]]
    print(sol.countIsland([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()