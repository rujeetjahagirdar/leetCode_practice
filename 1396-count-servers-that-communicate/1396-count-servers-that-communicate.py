class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # #dfs
        # #start from every server
        # #search in all directions till first occurance


        # visited = set()
        # ans=0
        # directions = [(1,0), (0,1), (0,-1), (-1,0)]


        # def dfs(i, j, ans):
            
        #     t=0

        #     for x in range(i+1, len(grid)):
        #         if(grid[x][j]==1):
        #             if((x,j) not in visited):
        #                 t+=1
        #                 visited.add((x,j))
        #             break
        #     for x in reversed(range(0, i)):
        #         if(grid[x][j]==1):
        #             if((x,j) not in visited):
        #                 t+=1
        #                 visited.add((x,j))
        #             break
        #     for y in range(j+1, len(grid[0])):
        #         if(grid[i][y]==1):
        #             if((i,y) not in visited):
        #                 t+=1
        #                 visited.add((i,y))
        #             break
        #     for y in reversed(range(0, j)):
        #         if(grid[i][y]==1):
        #             if((i,y) not in visited):
        #                 t+=1
        #                 visited.add((i,y))
        #             break
        #     print(t)
        #     if(t>0 and (i,j) not in visited):
        #         visited.add((i, j))
        #         return t+1
        #     return t




        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if(grid[i][j]==1):
        #             ans+=dfs(i, j, ans)
        
        # print(ans)
        # return ans

#############################
        rowServerCount = defaultdict(int)
        colServerCount = defaultdict(int)

        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    rowServerCount[i]+=1
                    colServerCount[j]+=1

        print(rowServerCount)
        print(colServerCount)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    if(rowServerCount[i]>1 or colServerCount[j]>1):
                        ans+=1
        print(ans)
        return ans