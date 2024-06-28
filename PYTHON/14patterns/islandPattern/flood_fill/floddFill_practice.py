class solution:
    def floodFill(self,matrix,x,y,newColor):

        if matrix[x][y]!=newColor:
            self.dfs_search(matrix,x,y,matrix[x][y],newColor)

        return matrix
    
    def dfs_search(self,matrix,x,y,oldColor,newColor):
        if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]):
            return 0 
        if matrix[x][y]!=oldColor:
            return 0
        
        matrix[x][y]=newColor

        self.dfs_search(matrix,x+1,y,oldColor,newColor)
        self.dfs_search(matrix,x-1,y,oldColor,newColor)
        self.dfs_search(matrix,x,y+1,oldColor,newColor)
        self.dfs_search(matrix,x,y-1,oldColor,newColor)

def main():
    sol = solution()


    matrix1 =[[0, 1, 1, 1, 0],
             [0, 0, 0, 1, 1],
               [0, 1, 1, 1, 0],
                 [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0]]
    
    print(sol.floodFill(matrix1,1,3,5))


main()