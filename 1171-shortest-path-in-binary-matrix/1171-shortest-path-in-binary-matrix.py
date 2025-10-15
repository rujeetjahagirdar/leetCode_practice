class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        #dfs

        if(grid[0][0]==1 or grid[-1][-1]==1):
            return -1
        
        directions = [(0,1), (0,-1), (1,0), (1,1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        visited = set()
        self.ans=0

        q = deque()
        q.append((0, 0, 1))

        while q:
            i, j, path_length = q.popleft()

            if(i==len(grid)-1 and j==len(grid[0])-1):
                return path_length
            
            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<=len(grid)-1 and 0<=newj<=len(grid[0])-1 and (newi, newj) not in visited and grid[newi][newj]==0):
                    q.append((newi, newj, path_length+1))
                    visited.add((newi, newj))        
        

        return -1