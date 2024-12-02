class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        directions = [(0, 1), (0, -1), (1,0), (-1,0)]

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j]==0):
                    q.append((i, j, 0))
        

        while q:
            r, c, l = q.popleft()
            
            for direction in directions:
                newr, newc = r+direction[0], c+direction[1]

                if(newr>=0 and newr<len(rooms) and newc>=0 and newc<len(rooms[0]) and rooms[newr][newc]==2147483647):
                    rooms[newr][newc]=l+1
                    q.append((newr, newc, l+1))