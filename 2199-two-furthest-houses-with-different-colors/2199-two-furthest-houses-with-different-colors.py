class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if(colors[j]!=colors[i]):
                    ans = max(ans, abs(i-j))
        
        return ans