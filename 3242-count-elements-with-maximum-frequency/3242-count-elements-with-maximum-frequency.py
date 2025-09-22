class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # c = Counter(nums)

        # mx = max(c.values())

        # print(mx)

        freq = defaultdict(int)
        mx = -1

        for i in nums:
            freq[i]+=1
            mx = max(mx, freq[i])

        ans=0

        for i in freq:
            if(freq[i]==mx):
                ans+=freq[i]
        
        return(ans)