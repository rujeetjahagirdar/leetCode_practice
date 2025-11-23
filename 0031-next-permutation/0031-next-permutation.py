class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,5,3,4,5,6] --> [1,2,5,3,4,6,5]

        #pivot will be an element where current number is less than next number

        i=len(nums)-2

        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        
        print(i)

        if(i>=0):
            #find element greater that nums[i] from right to left
            j=len(nums)-1
            while(j>i and nums[j]<=nums[i]):
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        
        l=i+1
        r = len(nums)-1

        while(l<r):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        print(nums)