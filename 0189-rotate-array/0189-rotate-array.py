class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        # j= k+1 if len(nums)%2!=0 else k
        # while(j<len(nums)):
        #     nums[i], nums[j] = nums[j], nums[i]
        #     i=i+1
        #     j=j+1
        # print(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
        print(nums)