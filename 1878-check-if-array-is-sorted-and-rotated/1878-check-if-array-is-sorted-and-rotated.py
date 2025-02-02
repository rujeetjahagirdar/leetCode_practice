class Solution:
    def check(self, nums: List[int]) -> bool:
        inversionCount = 0

        for i in range(1, len(nums)):
            if(nums[i]<nums[i-1]):
                inversionCount+=1
        if(nums[0]<nums[-1]):
            inversionCount+=1
        
        return inversionCount<=1