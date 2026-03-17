class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                if(matrix[r][c]==1):
                    matrix[r][c] +=matrix[r-1][c]
        
        print(matrix)
        ans=float('-inf')

        for r in range(len(matrix)):
            sorted_row = sorted(matrix[r], reverse=True)
            for i in range(len(sorted_row)):
                ans = max(ans, sorted_row[i]*(i+1))
        
        print(ans)
        return ans