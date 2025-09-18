class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = {0: 1}

        cumm_sum = 0
        ans=0

        for i in nums:
            cumm_sum +=i

            if(cumm_sum-k in count):
                ans+=count[cumm_sum-k]

            count[cumm_sum] = count.get(cumm_sum, 0)+1
        
        return(ans)