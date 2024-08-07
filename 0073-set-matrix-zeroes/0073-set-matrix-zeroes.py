class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashM = {'row':[],'col':[]}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    hashM['row'].append(i)
                    hashM['col'].append(j)
        print(hashM)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in hashM['row'] or j in hashM['col']:
                    matrix[i][j]=0
        print(matrix)