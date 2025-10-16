class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row_set = {}
        col_set = {}

        for i in range(len(matrix)):
            row_set[i] = set()
            col_set[i] = set()
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row_set[i].add(matrix[i][j])
                col_set[j].add(matrix[i][j])
        
        for i in range(len(matrix)):
            if(len(row_set[i])!=len(matrix)):
                return False
            if(len(col_set[i])!=len(matrix)):
                return False
        
        return True