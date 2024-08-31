class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in c:
            if(c[i]>2):
                return False
        return True