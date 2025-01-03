class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashM = {}

        for i in range(len(nums)):
            hashM[nums[i]]=i
        
        print(hashM)

        for i,j in operations:
            original_idx = hashM[i]
            nums[original_idx]=j
            hashM[j]=original_idx
        
        print(nums)
        return nums