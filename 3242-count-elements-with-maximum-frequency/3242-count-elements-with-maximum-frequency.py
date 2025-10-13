class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # c = Counter(nums)
        # ans=0
        # mxFreq = max(c.values())
        # for i in c:
        #     if(c[i]==mxFreq):
        #         ans+=c[i]
        
        # return ans


        freq = {}
        ans=0

        mxFreq = 0

        for i in nums:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1

            if(freq[i]==mxFreq):
                ans+=freq[i]
            elif(freq[i]>mxFreq):
                mxFreq = freq[i]
                ans=freq[i]
        
        return ans