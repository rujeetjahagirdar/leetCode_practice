class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c:
            if c[i]==1:
                return i