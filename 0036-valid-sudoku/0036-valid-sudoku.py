class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    if(board[i][j] in rowSet[i]):
                        return False
                    else:
                        rowSet[i].add(board[i][j])
                    if(board[i][j] in colSet[j]):
                        return False
                    else:
                        colSet[j].add(board[i][j])
                    if(board[i][j] in boxSet[(i//3,j//3)]):
                        return False
                    else:
                        boxSet[(i//3,j//3)].add(board[i][j])
        
        print(rowSet)
        print(colSet)
        print(boxSet)
        return True