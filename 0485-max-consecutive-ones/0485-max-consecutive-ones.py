class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        tempcount=0
        for i in range(len(nums)):
            if(nums[i]==1):
                tempcount +=1
            else:
                if(tempcount>ans):
                    ans=tempcount
                tempcount = 0
        if(tempcount>ans):
                ans=tempcount
        return(ans)
                    