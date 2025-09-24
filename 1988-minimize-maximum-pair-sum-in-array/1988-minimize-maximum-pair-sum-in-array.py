class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans=-1

        nums.sort()
        print(nums)
        l=0
        r=len(nums)-1

        while(l<r):
            ans = max(ans, (nums[l]+nums[r]))
            l+=1
            r-=1
        print(ans)
        return ans