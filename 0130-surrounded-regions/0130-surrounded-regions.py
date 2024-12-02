class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        def dfs(r, c):
            if((r, c) in visited):
                return 
            visited.add((r, c))
            board[r][c]='T'
            for direction in directions:
                newr, newc = r+ direction[0], c+ direction[1]
                if(newr>=0 and newr<len(board) and newc>=0 and newc<len(board[0]) and (newr, newc) not in visited and board[newr][newc]=='O'):
                    dfs(newr, newc)


        #1 Mark all regions which are on border as T
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='O'):
                    if(i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1):
                        dfs(i, j)

        #2 Mark all non border regions as X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='O'):
                    board[i][j]='X'
        #3 Revert all border regions from T to X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='T'):
                    board[i][j]='O'
        print(board)