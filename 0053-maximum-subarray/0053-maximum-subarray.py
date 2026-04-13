class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # #for every index, either the subrarry will end at current index or it will start from current index
        # dp = []
        # dp.append(nums[0])

        # for i in range(1, len(nums)):
        #     dp.append(max(dp[-1]+nums[i], nums[i]))
        
        # return max(dp)

        current_sum=nums[0]
        max_sum=nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum