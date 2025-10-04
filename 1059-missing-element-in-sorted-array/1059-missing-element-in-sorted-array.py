class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)-1):
            if((nums[i+1]-nums[i])-1>=k):
                return nums[i]+k
            else:
                k-=((nums[i+1]-nums[i])-1)
        return nums[-1]+k