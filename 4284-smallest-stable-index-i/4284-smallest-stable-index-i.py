class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mxVal = float("-INF")
        mnVal = float("INF")

        for i in range(len(nums)):
            mxVal = max(mxVal, nums[i])
            mnVal = min(nums[i:])

            if(mxVal - mnVal <=k):
                return i
        
        return -1