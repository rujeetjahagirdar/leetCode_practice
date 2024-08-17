class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        totalPeri = 0
        sharedPeri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    totalPeri +=4
                    if(j-1>=0 and grid[i][j-1]==1):
                        sharedPeri +=1
                    if(j+1<len(grid[0]) and grid[i][j+1]==1):
                        sharedPeri +=1
                    if(i-1>=0 and grid[i-1][j]==1):
                        sharedPeri +=1
                    if(i+1<len(grid) and grid[i+1][j]==1):
                        sharedPeri +=1
        print(totalPeri)
        print(sharedPeri)
        return (totalPeri - sharedPeri)