class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mxVal = nums[0]
        mnVal = min(nums)

        for i in range(len(nums)):
            if(nums[i]>=mxVal):
                mxVal = nums[i]
            if(nums[i]>=mnVal):
                mnVal = min(nums[i:])
            
            print(f"mxVal = {mxVal}, mnVal = {mnVal}")
            
            instability = mxVal - mnVal

            if(instability<=k):
                return i
        
        return -1