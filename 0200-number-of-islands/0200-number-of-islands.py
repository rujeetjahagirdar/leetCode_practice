class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        visited = set()
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        def dfs(i, j):
            visited.add((i, j))

            for direction in directions:
                new_i, new_j = i+ direction[0], j+direction[1]

                if(0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and (new_i, new_j) not in visited and grid[new_i][new_j]=='1'):
                    dfs(new_i, new_j)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1" and (i, j) not in visited):
                    ans+=1
                    dfs(i,j)
        
        return(ans)