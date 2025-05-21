class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        max_time=0
        fresh_count=0
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    q.append((i, j, 0))
                elif(grid[i][j]==1):
                    fresh_count +=1
        
        while(q and fresh_count>0):
            i, j, d = q.popleft()

            for direction in directions:
                new_i, new_j = direction[0]+i, direction[1]+j
                if(0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==1):
                    grid[new_i][new_j] = 2
                    fresh_count-=1
                    q.append((new_i, new_j, d+1))
                    max_time = max(max_time, d+1)

        print(max_time)
        if(fresh_count==0):
            return max_time
        return -1