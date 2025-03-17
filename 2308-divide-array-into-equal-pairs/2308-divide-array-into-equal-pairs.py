class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for i in c:
            if(c[i]%2!=0):
                return False
        
        return True