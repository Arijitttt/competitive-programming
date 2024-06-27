class solution:
    def countIsland(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIsland = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    totalIsland+=1
                    self.visit_is_land_DFS(matrix,i,j)
        return totalIsland

    def visit_is_land_DFS(self,matrix,x,y):
        if(x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0])):
            return
        if matrix[x][y] == 0:
            return


        matrix[x][y] = 0

        self.visit_is_land_DFS(matrix,x+1,y)
        self.visit_is_land_DFS(matrix,x-1,y)
        self.visit_is_land_DFS(matrix,x,y+1)
        self.visit_is_land_DFS(matrix,x,y-1)


def main():

    sol = solution()

    matrix = [[0, 1, 1, 1, 0],
               [0, 0, 0, 1, 1],
                 [0, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]]

    print(sol.countIsland(matrix))


main()