class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        # c = Counter(nums)
        # ans=0
        # mxFreq = max(c.values())
        # for i in c:
        #     if(c[i]==mxFreq):
        #         ans+=c[i]
        # return ans


        mxFreq= 0
        ans=0

        freq = defaultdict(int)

        for n in nums:
            freq[n]+=1

            if(freq[n]>mxFreq):
                mxFreq = freq[n]
                ans=freq[n]
            elif(freq[n]==mxFreq):
                ans+=freq[n]
        return ans