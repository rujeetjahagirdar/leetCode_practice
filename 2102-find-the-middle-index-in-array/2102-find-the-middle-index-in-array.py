class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum-=nums[i]
            if(leftSum==rightSum):
                print(i)
                return i
            leftSum+=nums[i]
        
        return -1