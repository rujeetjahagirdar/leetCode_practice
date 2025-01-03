class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        minDiff = float("inf")
        ans=0
        n=len(nums)

        for i in range(len(nums)):
            leftSum +=nums[i]
            rightSum -=nums[i]

            leftAvg = int(leftSum/(i+1))
            # rightAvg = int(rightSum/(n-i-1))
            if(n-i-1>0):
                rightAvg = int(rightSum/(n-i-1))
            else:
                rightAvg = 0
            # minDiff = min(minDiff, abs(leftAvg-rightAvg))
            if(abs(leftAvg-rightAvg)<minDiff):
                minDiff = abs(leftAvg-rightAvg)
                ans=i
        print(minDiff)
        print(ans)
        return ans