class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        #bfs

        q = deque()
        visited = set()

        directoins = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        if(grid[0][0]!=0 or grid[-1][-1]!=0):
            return -1
        
        q.append((0, 0, 1))
        visited.add((0, 0))



        while q:
            for _ in range(len(q)):
                i, j, path_length = q.popleft()

                if(i==len(grid)-1 and j==len(grid[0])-1):
                    return path_length
                
                for direction in directoins:
                    newi, newj = i+direction[0], j+direction[1]

                    if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited and grid[newi][newj]==0):
                        q.append((newi, newj, path_length+1))
                        visited.add((newi, newj))
        
        return -1