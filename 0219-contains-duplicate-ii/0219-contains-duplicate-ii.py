class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)-1):
        #     j = i+1
        #     while(j<=i+k and j<len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True
        #         j +=1
        # return False
        
        hashM = {}
        for i in range(len(nums)):
            if nums[i] in hashM and abs(i - hashM[nums[i]])<=k:
                return True
            else:
                hashM[nums[i]] = i
        return False