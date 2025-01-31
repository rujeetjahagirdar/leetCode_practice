class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islandMap = defaultdict(set)
        islandSize = defaultdict(int) 

        isLandId = 1000

        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, iId):
            size=1
            visited.add((i, j))
            islandMap[iId].add((i, j))
            grid[i][j]=iId
            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]
                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited and grid[newi][newj]==1):
                    # islandMap[iId].add((newi, newj))
                    size +=dfs(newi, newj, iId)

            return size        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((i, j) not in visited and grid[i][j]==1):
                    visited.add((i, j))
                    islandMap[isLandId].add((i, j))
                    # print(islandMap[isLandId])
                    s=dfs(i, j, isLandId)
                    islandSize[isLandId]=s
                    isLandId+=1
        
        print(islandMap)
        print(islandSize)
        print(grid)

        ans=float("-inf")

        #for each 0, 
            #check if there are neighbouring islands
        
        if(len(islandSize)==1 and islandSize[1000]==(len(grid)*len(grid))):
            return islandSize[1000]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    t=1
                    neighbourIslands = set()
                    for direction in directions:
                        ni, nj = i+direction[0], j+direction[1]
                        if(0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]>=1000 and grid[ni][nj] not in neighbourIslands): #is part of any island
                            neighbourIslands.add(grid[ni][nj])
                            t+=islandSize[grid[ni][nj]]
                    
                    ans=max(ans, t)
        
        print(ans)
        return ans