class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=r=0
        ans = 0
        k=1

        while(r<len(nums)):
            if(nums[r]==0):
                k-=1
            
            while(k<0):
                if(nums[l]==0):
                    k+=1
                l+=1
            
            ans = max(ans, (r-l)+1)

            r+=1
        
        print(ans-1)
        return ans-1

