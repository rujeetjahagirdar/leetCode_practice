class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        #while r<len nums
            #expand while 1s or (0 and k>0)
                #expand
            #else
                #check max length
                #shrink from left until k becomes >0

        ans = 0

        l=0

        for r in range(len(nums)):
            if(nums[r]==0):
                k-=1
            
            while(k<0):
                if(nums[l]==0):
                    k+=1
                l+=1
            ans = max(ans, (r-l+1))
        return ans