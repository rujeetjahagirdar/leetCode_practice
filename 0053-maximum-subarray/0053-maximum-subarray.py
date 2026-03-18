class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #for every index, either the subrarry will end at current index or it will start from current index
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            dp.append(max(dp[-1]+nums[i], nums[i]))
        
        return max(dp)