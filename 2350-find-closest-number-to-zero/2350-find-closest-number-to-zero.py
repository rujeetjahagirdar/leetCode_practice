class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = []
        minV = float('inf')
        for i in nums:
            if(abs(i)<minV):
                minV = abs(i)
        for i in nums:
            if(abs(i)==minV):
                ans.append(i)
        return max(ans)