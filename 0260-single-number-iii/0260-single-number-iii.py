class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        c = Counter(nums)
        for i in c:
            if c[i]==1:
                ans.append(i)
        return ans