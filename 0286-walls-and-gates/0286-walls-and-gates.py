class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #multipoint bfs

        q = deque()
        visited = set()

        directions = [(0, 1), (1,0), (0, -1), (-1, 0)]

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j]==0):
                    visited.add((i, j))
                    q.append((i, j, 0))
        
        while q:
            i, j, d = q.popleft()

            rooms[i][j]=d

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(rooms) and 0<=newj<len(rooms[0]) and (newi, newj) not in visited and rooms[newi][newj] not in (0, -1)):
                    visited.add((newi, newj))
                    q.append((newi, newj, d+1))
        