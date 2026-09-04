class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # mxVal = float("-INF")
        # mnVal = float("INF")

        # for i in range(len(nums)):
        #     mxVal = max(mxVal, nums[i])
        #     mnVal = min(nums[i:])

        #     if(mxVal - mnVal <=k):
        #         return i
        
        # return -1

        mins = [-1]*len(nums)
        mins[-1] = nums[-1]

        for i in reversed(range(len(nums)-1)):
            mins[i] = min(nums[i], mins[i+1])
        
        # print(mins)

        mxVal = float("-INF")

        for i in range(len(nums)):
            mxVal = max(mxVal, nums[i])

            if((mxVal - mins[i]) <=k):
                return i
        
        return -1