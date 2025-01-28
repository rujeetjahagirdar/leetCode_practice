class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        if(len(grid)==1 and len(grid[0])==1):
            return grid[0][0]
        
        
        ans=0

        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        visited = set()
        

        def dfs(i, j):
            t=grid[i][j]
            visited.add((i,j))

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]
                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited and grid[newi][newj]>0):
                    t+=dfs(newi, newj)

            return t

        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]>0 and (i,j) not in visited):
                    visited.add((i,j))
                    ans=max(ans,dfs(i,j))

        
        print(ans)
        return ans