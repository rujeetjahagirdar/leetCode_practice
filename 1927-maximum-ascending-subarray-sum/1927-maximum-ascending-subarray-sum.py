class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=0

        if(len(nums)==1):
            return nums[0]

        t = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                t+=nums[i]
            else:
                ans=max(t, ans)
                t=nums[i]
        ans=max(ans, t)
        print(ans)
        return ans