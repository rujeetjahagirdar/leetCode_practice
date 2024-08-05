class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashM:
                return [i, hashM[compliment]]
            else:
                hashM[nums[i]] = i