# from statistics import mode
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans=0
        c = Counter(nums)
        maxFreq = max(c.values())
        for i in c:
            if(c[i]==maxFreq):
                ans +=c[i]
        return ans