class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans=0

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if(board[i][j]=='X'):
        #             if(i>0 and board[i-1][j]=='X'):
        #                 continue
        #             if(j>0 and board[i][j-1]=='X'):
        #                 continue
        #             ans+=1
        # return ans


        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='X'):
                    # if(i==0):
                    #     if(j>0 and board[i][j-1]!='X'):
                    #         ans+=1
                    #     elif(j==0):
                    #         ans+=1
                    # elif(j==0):
                    #     if(i>0 and board[i-1][j]!='X'):
                    #         ans+=1
                    if(i==0 and j==0):
                        ans+=1
                        continue
                    if(i==0 and board[i][j-1]!='X'):
                        ans+=1
                        continue
                    if(j==0 and board[i-1][j]!='X'):
                        ans+=1
                        continue
                    if(i>0 and j>0):
                        if(board[i-1][j]!='X' and board[i][j-1]!='X'):
                            ans+=1
                # print(ans)
        print(ans)
        return ans
