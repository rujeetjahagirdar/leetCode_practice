class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #use cummulative sum counter

        cummSumCounter = {0: 1}
        cummSum = 0
        ans=0

        for n in nums:
            cummSum+=n

            if((cummSum - k) in cummSumCounter):
                ans+=cummSumCounter[(cummSum - k)]
            
            cummSumCounter[cummSum] = cummSumCounter.get(cummSum, 0)+1
        
        return(ans)