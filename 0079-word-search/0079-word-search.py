class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i, j, remainingWord):
            if(remainingWord==''):
                return True
            
            # if(board[i][j]==remainingWord[0]):

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]

                if(0<=newi<len(board) and 0<=newj<len(board[0]) and (newi, newj) not in visited and board[newi][newj]==remainingWord[0]):
                    visited.add((newi, newj))
                    if dfs(newi, newj, remainingWord[1:]):
                        return True
                    
                    visited.remove((newi, newj))
            
            
            return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]):
                    visited.add((i, j))
                    if dfs(i, j, word[1:]):
                        return True
                    visited.remove((i, j))
        
        return False
