class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = float('-inf')

        for i in range(len(nums)-1):
            ans = max(ans, abs(nums[i+1]-nums[i]))
        
        ans = max(ans, abs(nums[0]-nums[-1]))

        return ans