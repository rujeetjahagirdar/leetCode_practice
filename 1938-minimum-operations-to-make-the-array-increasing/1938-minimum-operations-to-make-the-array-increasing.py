class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0

        for i in range(1, len(nums)):
            if(nums[i]<=nums[i-1]):
                ans+=(nums[i-1]-nums[i])+1
                nums[i]+=(nums[i-1]-nums[i])+1
        
        return ans