class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=float('-inf')

        l=0
        r=0
        windowSum=0

        while(r<len(nums)):
            if((r-l)<k):
                windowSum+=nums[r]
            else:
                windowSum+=nums[r]
                windowSum-=nums[l]
                l+=1
            
            if((r-l)==k-1):
                ans = max(ans, windowSum/k)
            
            r+=1
        
        return ans