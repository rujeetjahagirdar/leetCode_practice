class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        prefix_mat = [[[0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # print(prefix_mat)
        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i==0 and j==0):
                    if(grid[i][j]=='X'):
                        prefix_mat[i][j][0]+=1
                    elif(grid[i][j]=='Y'):
                        prefix_mat[i][j][1]+=1
                elif(i==0 and j>0):
                    if(grid[i][j]=='X'):
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]+1
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1]
                    elif(grid[i][j]=='Y'):
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1]+1
                    else:
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1]
                elif(i>0 and j==0):
                    if(grid[i][j]=='X'):
                        prefix_mat[i][j][0] = prefix_mat[i-1][j][0]+1
                        prefix_mat[i][j][1] = prefix_mat[i-1][j][1]
                    elif(grid[i][j]=='Y'):
                        prefix_mat[i][j][0] = prefix_mat[i-1][j][0]
                        prefix_mat[i][j][1] = prefix_mat[i-1][j][1]+1
                    else:
                        prefix_mat[i][j][0] = prefix_mat[i-1][j][0]
                        prefix_mat[i][j][1] = prefix_mat[i-1][j][1]
                else:
                    if(grid[i][j]=='X'):
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]+prefix_mat[i-1][j][0]-prefix_mat[i-1][j-1][0]+1
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1] + prefix_mat[i-1][j][1] - prefix_mat[i-1][j-1][1]
                    elif(grid[i][j]=='Y'):
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]+prefix_mat[i-1][j][0]-prefix_mat[i-1][j-1][0]
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1] + prefix_mat[i-1][j][1] - prefix_mat[i-1][j-1][1]+1
                    else:
                        prefix_mat[i][j][0] = prefix_mat[i][j-1][0]+prefix_mat[i-1][j][0]-prefix_mat[i-1][j-1][0]
                        prefix_mat[i][j][1] = prefix_mat[i][j-1][1] + prefix_mat[i-1][j][1] - prefix_mat[i-1][j-1][1]

                # print(prefix_mat)

                if(prefix_mat[i][j][0]==prefix_mat[i][j][1] and prefix_mat[i][j][0]>=1):
                    ans+=1
        
        print(ans)
        return ans