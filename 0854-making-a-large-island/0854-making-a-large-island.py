class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        #keep a mapping for islandID: size
        #for every 0, check if there are any neighbouring islands.

        #dfs, bottom-up

        #[1,0]
        #[1,1]

        def dfs(i, j, iId):
            iSize = 1
            grid[i][j]=iId

            for direction in directions:
                new_i, new_j = i+direction[0], j+direction[1]

                if(0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==1):
                    iSize += dfs(new_i, new_j, iId)
            
            return iSize
        
        islandSizeMap = {}
        islandId = 100
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        ans=float("-inf")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    islandSize = dfs(i, j, islandId)

                    islandSizeMap[islandId] = islandSize
                    islandId+=1
        print(islandSizeMap)
        print(grid)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    if(len(islandSizeMap)==0): #case:all water
                        return 1
                        
                    totalSize=0
                    visited_neighbours = set()
                    #check neighbours
                    for direction in directions:
                        newi, newj = i+direction[0], j+direction[1]

                        if(0<=newi<len(grid) and 0<=newj<len(grid) and grid[newi][newj] not in visited_neighbours and grid[newi][newj]>=100):
                            visited_neighbours.add(grid[newi][newj])
                            totalSize += islandSizeMap[grid[newi][newj]]
                        
                        print(visited_neighbours)
                    
                    ans = max(ans, totalSize+1)
        

        #case:all island
        if(ans==float("-inf") and len(islandSizeMap)==1): #no 0 found in grid
            return islandSizeMap[100]

        # #case:all water
        # if(len(islandSizeMap)==0):
        #     return 1
        
        
        return ans