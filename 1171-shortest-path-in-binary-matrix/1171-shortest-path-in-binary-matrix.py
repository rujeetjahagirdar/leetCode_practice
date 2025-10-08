class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        #edge case, when (0,0) element is 1 or last element is 1

        
        directions = [(1,0), (0,1), (1,1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]

        visited = set()

        m = len(grid)-1
        n = len(grid[0])-1


        if(grid[0][0]==1 or grid[m][n]==1):
            return -1


        q = deque()
        q.append((0,0, 1))

        while q:

            x, y, length = q.popleft()
            if(x==m and y==n):
                return length
            
            for direction in directions:
                newx, newy = x+direction[0], y+direction[1]

                if(0<=newx<=m and 0<=newy<=n and (newx, newy) not in visited and grid[newx][newy]==0):
                    q.append((newx, newy, length+1))
                    visited.add((newx, newy))
        return -1