class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        cummSum = 0

        for i in range(len(nums)):
            # cummSum+=nums[i]

            if(cummSum==(total - cummSum - nums[i])):
                return i
            
            cummSum+=nums[i]
        return -1