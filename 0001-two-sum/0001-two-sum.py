class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if(nums[j]==(target-nums[i])):
#                     return [i,j]
        
        ##########
        hashM = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashM:
                return [i, hashM[compliment]]
            else:
                hashM[nums[i]] = i