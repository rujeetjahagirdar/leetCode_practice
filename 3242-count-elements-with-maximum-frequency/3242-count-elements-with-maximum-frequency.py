class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)

        mx = max(c.values())

        print(mx)

        ans=0

        for i in c:
            if(c[i]==mx):
                ans+=c[i]
        
        return(ans)