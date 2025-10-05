class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i in range(len(nums)):
            if(target- nums[i] in hashM):
                return [hashM[target-nums[i]], i]
            else:
                hashM[nums[i]]=i
