class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        s = sum(nums)

        if(s<k):
            return s
        
        return s%k