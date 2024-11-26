class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = float('-inf')
        for r in matrix:
            flipped_r = [0 if i==1 else 1 for i in r]
            t=0
            for row in matrix:
                if(row==r or row==flipped_r):
                    t+=1
            ans = max(ans, t)
        
        print(ans)
        return ans