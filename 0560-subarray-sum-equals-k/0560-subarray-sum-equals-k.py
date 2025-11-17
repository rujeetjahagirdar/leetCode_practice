class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #use cummulative sum counter

        cummulativeSum=0
        cummulativeSumFreq = {0: 1}
        ans=0

        for i in nums:
            cummulativeSum+=i

            if((cummulativeSum - k) in cummulativeSumFreq):
                ans+=cummulativeSumFreq[(cummulativeSum - k)]
            
            cummulativeSumFreq[cummulativeSum] = cummulativeSumFreq.get(cummulativeSum, 0) +1
        
        return ans