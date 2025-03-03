class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # in each operation, one number is eliminated
            # so answer will be number of unique non zero numbers
        
        uniq = set()
        for i in nums:
            if(i>0):
                uniq.add(i)
        
        return len(uniq)