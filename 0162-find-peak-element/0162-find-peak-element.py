class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if(len(nums)<=4):
        #     return (nums.index(max(nums)))
        left =0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid + 1]:  # If the mid element is greater than its right neighbor
                right = mid
            else:
                left = mid + 1
                
        return left