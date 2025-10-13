class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashM = {}

        for i in range(len(nums)):
            if(nums[i] in hashM):
                if((i - hashM[nums[i]]) <=k):
                    return True
            hashM[nums[i]] = i
        return False