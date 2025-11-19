class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        #same diagonal indexs will have same sum of r+c

        diagonals = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if((i-j) in diagonals):
                    if(matrix[i][j]!=diagonals[i-j]):
                        return False
                else:
                    diagonals[i-j] = matrix[i][j]
        
        return True