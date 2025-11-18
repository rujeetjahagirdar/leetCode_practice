class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        #mark islands using dfs
        #find shorted distance using bfs

        def dfs(i, j, iId):
            grid[i][j]=iId

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]==1):
                    dfs(newi, newj, iId)
        
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        iId = 100
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #mark first island
                if(grid[i][j]==1):
                    dfs(i, j, iId)
                    iId+=1
        
        print(grid)

        #multipoint bfs

        q = deque()
        visited = set()
        ans=float("inf")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==100):
                    visited.add((i, j))
                    q.append((i, j, 0))
        
        while q:
            i, j, d = q.popleft()
            #if another island reached, update anser
            #else
                #increase distance
                #explore neighbours, if water, add to queue
            if(grid[i][j]==0):
                d+=1
            if(grid[i][j]==101):
                ans = min(ans, d)
            
            # d=d+1

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited):
                    visited.add((newi, newj))
                    q.append((newi, newj, d))

        return(ans)