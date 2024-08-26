class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        nextState = {0: [], 1: []}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                liveN=0
                # if(0<=i-1<m):
                #     if(0<=j-1<n):
                #         if board[i-1][j-1] ==1:
                #             liveN +=1
                #     if(0<=j<n):
                #         if board[i-1][j] ==1:
                #             liveN +=1
                #     if(0<=j+1<n):
                #         if board[i-1][j+1] ==1:
                #             liveN +=1
                # if(0<=i<m):
                #     if(0<=j-1<n):
                #         if board[i][j-1] ==1:
                #             liveN +=1
                #     # if(0<=j<n):
                #     #     if board[i][j] ==1:
                #     #         liveN +=1
                #     if(0<=j+1<n):
                #         if board[i][j+1] ==1:
                #             liveN +=1
                # if(0<=i+1<m):
                #     if(0<=j-1<n):
                #         if board[i+1][j-1] ==1:
                #             liveN +=1
                #     if(0<=j<n):
                #         if board[i+1][j] ==1:
                #             liveN +=1
                #     if(0<=j+1<n):
                #         if board[i+1][j+1] ==1:
                #             liveN +=1
                for d in directions:
                    newi, newj = i+d[0], j+d[1]
                    if(0<=newi<m and 0<=newj<n):
                        if(board[newi][newj]==1):
                            liveN +=1

                print(i,j, liveN)
                if(board[i][j]==1):
                    if(liveN<2):
                        nextState[0].append((i,j))
                    elif(2<=liveN<=3):
                        nextState[1].append((i,j))
                    elif(liveN>3):
                        nextState[0].append((i,j))
                else:
                    if(liveN==3):
                        nextState[1].append((i,j))
        for i in range(m):
            for j in range(n):
                if((i,j) in nextState[0]):
                    board[i][j]=0
                if((i,j) in nextState[1]):
                    board[i][j]=1
        print(board)