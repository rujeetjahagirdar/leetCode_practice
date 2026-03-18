class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        prefix_matrix = [[0] * c for _ in range(r)]
        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i==0 and j==0):
                    prefix_matrix[i][j] = grid[i][j]
                elif(i>0 and j==0):
                    prefix_matrix[i][j] = prefix_matrix[i-1][j] + grid[i][j]
                elif(i==0 and j>0):
                    prefix_matrix[i][j] = prefix_matrix[i][j-1] + grid[i][j]
                else:
                    prefix_matrix[i][j] = prefix_matrix[i][j-1] + prefix_matrix[i-1][j] + prefix_matrix[i-1][j-1] - 2*prefix_matrix[i-1][j-1] + grid[i][j]
                
                if(prefix_matrix[i][j]<=k):
                    ans+=1
        
        return(ans)