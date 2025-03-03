class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = ['_']*len(nums)

        l=0
        r=len(nums)-1

        for i in range(len(nums)):
            if(nums[i]<pivot):
                ans[l]=nums[i]
                l+=1
        
        for i in reversed(range(len(nums))):
            print(nums[i])
            if(nums[i]>pivot):
                ans[r]=nums[i]
                r-=1
        
        for i in range(len(ans)):
            if(ans[i]=='_'):
                ans[i]=pivot
        
        print(ans)
        return ans