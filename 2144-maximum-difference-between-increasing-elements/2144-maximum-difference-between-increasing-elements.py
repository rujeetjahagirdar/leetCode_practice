class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min = [0]*len(nums)
        mn = nums[0]

        for i in range(len(nums)):
            prefix_min[i] = mn
            mn = min(mn, nums[i])
        
        print(prefix_min)
        ans=-1

        for i in range(len(nums)):
            if(prefix_min[i]<nums[i]):
                ans = max(ans, (nums[i]-prefix_min[i]))
        
        return(ans)