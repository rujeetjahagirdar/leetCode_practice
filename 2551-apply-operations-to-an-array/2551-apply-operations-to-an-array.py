class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        #[1,1,2,2,2,2,2,3,4,5,5]

        i=0
        while(i<len(nums)-1):
            if(nums[i+1]==nums[i]):
                nums[i]*=2
                nums[i+1]=0
            i+=1
            # print(nums)

        for i in range(len(nums)-1):
            if(nums[i]==0):
                j=i+1
                while(j<len(nums) and nums[j]==0):
                    j+=1
                if(j>=len(nums)):
                    # print(nums)
                    return nums
                else:
                    nums[i]=nums[j]
                    nums[j]=0
                # print(nums)
        return nums