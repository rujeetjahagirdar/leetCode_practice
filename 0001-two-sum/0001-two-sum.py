class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i in range(len(nums)):
            if((target - nums[i]) in hashM):
                idx = hashM[target - nums[i]]
                return [idx, i]
            else:
                hashM[nums[i]] = i
            # print(hashM)
        return -1