class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if((target - nums[i]) in hashMap):
                return [hashMap[(target-nums[i])], i]
            else:
                hashMap[nums[i]]=i
        
