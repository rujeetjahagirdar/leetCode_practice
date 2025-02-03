class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=0
        curr = 1
        for i in range(1, len(nums)):
            # curr=1
            if(nums[i-1]<nums[i]):
                curr+=1
            else:
                ans=max(ans, curr)
                curr=1
        ans=max(ans, curr)
        print(ans)

        ans2=0
        curr = 1
        for i in range(len(nums)-1):
            # curr=1
            if(nums[i]>nums[i+1]):
                curr+=1
                # print(curr)
            else:
                ans2=max(ans2, curr)
                curr=1
        ans2=max(ans2, curr)
        print(ans2)

        return max(ans, ans2)