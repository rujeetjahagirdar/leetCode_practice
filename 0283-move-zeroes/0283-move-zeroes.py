class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[position]=nums[i]
                position = position+1
        for i in range(position,len(nums)):
            nums[i]=0
        # print(nums)