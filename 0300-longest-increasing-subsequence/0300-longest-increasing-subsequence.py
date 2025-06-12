class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prefix_lis = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if(nums[j]>nums[i]):
                    prefix_lis[i] = max(prefix_lis[i], 1+prefix_lis[j])
        
        print(prefix_lis)
        return max(prefix_lis)