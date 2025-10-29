class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cummSum = 0
        hashM = {0: 1}
        ans=0

        for n in nums:
            cummSum+=n

            if((cummSum-k) in hashM):
                ans+=hashM[(cummSum-k)]
            
            hashM[cummSum] = hashM.get(cummSum, 0)+1
        
        return(ans)