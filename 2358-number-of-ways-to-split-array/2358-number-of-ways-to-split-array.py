class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        ans=0


        for i in range(len(nums)-1):
            leftSum +=nums[i]
            rightSum -=nums[i]

            if(leftSum>=rightSum):
                ans+=1
        
        print(ans)
        return ans