from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited= set()
        islandCount=0
        
        def bfs(i,j):
            q.append((i,j))
            visited.add((i,j))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            while q:
                r, c = q.popleft()
                for d in directions:
                    newr, newc = r+d[0], c+d[1]
                    if(newr in range(len(grid)) and newc in range(len(grid[0])) and (newr,newc) not in visited and grid[newr][newc]=='1'):
                        q.append((newr, newc))
                        visited.add((newr,newc))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1' and (i,j) not in visited):
                    bfs(i,j)
                    islandCount = islandCount +1
        return islandCount