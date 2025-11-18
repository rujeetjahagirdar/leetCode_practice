class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        #bfs
        i, j = click

        if(board[i][j]=='M'):
            board[i][j]='X'

            return board
        
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        q = deque()
        q.append((i, j))
        visited = set()
        visited.add((i, j))

        while q:
            i, j = q.popleft()

            #check number of mines in neighbours
            nMine = 0

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(board) and 0<=newj<len(board[0]) and board[newi][newj]=='M'):
                    nMine+=1
            
            if(nMine>0):
                board[i][j]=str(nMine)
            else:
                board[i][j]='B'
                for direction in directions:
                    newi, newj = i+direction[0], j+direction[1]

                    if(0<=newi<len(board) and 0<=newj<len(board[0]) and (newi, newj) not in visited and board[newi][newj]=='E'):
                        visited.add((newi, newj))
                        q.append((newi, newj))
        
        return(board)