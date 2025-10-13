class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans=0
        mxFreq = max(c.values())
        for i in c:
            if(c[i]==mxFreq):
                ans+=c[i]
        
        return ans