class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        ans=0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0 and (i, j) not in visited):
                    
                    ans+=1
                    visited.add((i, j))
                    q.append((i, j))
                    isBoundryCell = False

                    while q:
                        m, n = q.popleft()

                        if(m==0 or m==len(grid)-1 or n==0 or n==len(grid[0])-1):
                            # ans-=1
                            isBoundryCell = True

                        for di, dj in directions:
                            newi, newj = m+di, n+dj

                            if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited and grid[newi][newj]==0):
                                visited.add((newi, newj))
                                q.append((newi, newj))
                    
                    if(isBoundryCell==True):
                        ans-=1
        
        print(ans)
        return ans