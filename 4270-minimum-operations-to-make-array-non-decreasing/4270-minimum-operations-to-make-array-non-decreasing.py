class Solution:
    def minOperations(self, nums: list[int]) -> int:
        maxSoFar = nums[0]
        diff=0

        for i in range(1, len(nums)):
            if(nums[i-1]-nums[i] <= 0):
                # diff+=0
                maxSoFar=nums[i]+diff
            else:
                diff+=nums[i-1]-nums[i]
                maxSoFar = nums[i]+diff
        
        return(diff)