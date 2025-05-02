class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualXOR = 0
        
        for i in range(len(nums)+1):
            actualXOR = actualXOR^i
        
        gotXOR = 0
        for i in nums:
            gotXOR = gotXOR^i
        
        return(actualXOR^gotXOR)