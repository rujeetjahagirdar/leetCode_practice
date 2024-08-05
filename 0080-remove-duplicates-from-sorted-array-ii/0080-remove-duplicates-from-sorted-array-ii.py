class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(nums):
            # print(nums)
            i = 0
            for j in range(len(nums)):
                if(nums[j]!="_"):
                    nums[i], nums[j] = nums[j], nums[i]
                    i=i+1
                    
        i, j = 0, 0
        count=0
        blankCount = 0
        while(i<len(nums)-1):
            # print(nums[i], i)
            count = 1
            j=i+1
            while(j<len(nums) and nums[i]==nums[j]):
                count = count +1
                if(count>2):
                    nums[j]='_'
                    blankCount=blankCount+1
                j = j+1
            i=j
        swap(nums)
        # print(nums)
        return(len(nums)-blankCount)
            # i = i+1