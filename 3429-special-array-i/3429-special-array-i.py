class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            # if((nums[i-1]%2!=0 and nums[i]%2!=0) or (nums[i-1]%2==0 and nums[i]%2==0)):
            if((nums[i-1]%2==nums[i]%2)):
                return False
        return True