class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #mark all islands by their ids
        #store island id to size mapping

        #trace all 0s, and check if there are any neighbouring islands, if yes, summ their sizes

        islandId = 100
        islandSize = {}

        #mark all islands, dfs

        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]

        def dfs(i, j, iId):
            size=1
            grid[i][j]=iId

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]
                
                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]==1):
                    size+=dfs(newi, newj, iId)

            return size

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    iSize = dfs(i, j, islandId)

                    islandSize[islandId] = iSize

                    islandId+=1
        
        print(islandSize)
        print(grid)

        ans=float("-inf")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    if(not islandSize): #no islands
                        return 1
                    #ceck neighiurs
                    neighbourSize=0
                    visitedNeighbour = set()
                    for direction in directions:
                        neighbouri, neighbourj = i+direction[0], j+direction[1]
                        if(0<=neighbouri<len(grid) and 0<=neighbourj<len(grid[0]) and grid[neighbouri][neighbourj] not in visitedNeighbour and grid[neighbouri][neighbourj]>=100):
                            visitedNeighbour.add(grid[neighbouri][neighbourj])
                            neighbourSize+=islandSize[grid[neighbouri][neighbourj]]
                    ans = max(ans, neighbourSize+1)
        
        print(ans)
        if(ans==float("-inf") and islandSize):
            ans = islandSize[100]
        
        return ans