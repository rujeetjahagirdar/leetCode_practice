class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans=0

        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col]=='X'):
                    if(row>0 and board[row-1][col]=='X'):
                        continue
                    if(col>0 and board[row][col-1]=='X'):
                        continue
                    ans+=1
        return(ans)