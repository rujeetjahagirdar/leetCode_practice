class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #dfs

        visited = set()
        ans = 0
        directions = [(0, 1), (1,0), (0, -1), (-1,0)]

        def dfs(i, j):
            a=1

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]==1 and (newi, newj) not in visited):
                    visited.add((newi, newj))
                    a+=dfs(newi, newj)
            
            return a


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1 and (i, j) not in visited):
                    visited.add((i, j))
                    area = dfs(i, j)
                    print(area)
                    ans = max(ans, area)
        return ans