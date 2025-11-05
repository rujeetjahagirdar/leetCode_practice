class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find index where its left element is less that this index element
        #

        pivot = -1

        for i in range(len(nums)-1, -1, -1):
            if(nums[i]>nums[i-1]):
                pivot = i-1
                break
        
        if(pivot!=-1):
            for j in range(len(nums)-1, pivot, -1):
                if(nums[j]>nums[pivot]):
                    break
            
            nums[pivot], nums[j] = nums[j], nums[pivot]
        
        #reverse numbers from next to pivot to end
        #two pointer
        l = pivot+1
        r = len(nums)-1

        while(l<=r):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        