class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maxAvg= float(-inf)
        # if(len(nums)==1):
        #     return sum(nums)/k
        # else:
        #     for i in range(len(nums)-k+1):
        #         # print(nums[i:i+k])
        #         if(sum(nums[i:i+k])/k>maxAvg):
        #             maxAvg = sum(nums[i:i+k])/k
        # # print(maxAvg)
        # return maxAvg
        windowSum = sum(nums[:k])
        maxSum = windowSum
        for i in range(k,len(nums)):
            windowSum = windowSum + nums[i] - nums[i-k]
            maxSum = max(maxSum, windowSum)
        return maxSum/k