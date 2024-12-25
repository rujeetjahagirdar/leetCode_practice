class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []

        if(nums==[]):
            return [[lower, upper]]
        if(upper==lower):
            return []
        

        for i in range(len(nums)+1):
            if(i==0 and nums[i]!=lower):
                ans.append([lower, nums[i]-1])
            elif(i==len(nums) and nums[i-1]!=upper):
                ans.append([nums[i-1]+1, upper])
                break
            elif(i>0 and i<len(nums)):
                if(nums[i]!=nums[i-1]+1):
                    ans.append([nums[i-1]+1, nums[i]-1])
        # if(nums[-1]!=99):
        #     ans.append([nums[-1]+1, 99])
        print(ans)
        return ans