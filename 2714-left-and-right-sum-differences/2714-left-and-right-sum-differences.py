class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]*len(nums)
        rightSum = [0]*len(nums)
        ans=[]

        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i-1]+nums[i-1]
            rightSum[-(i+1)] = rightSum[-(i+1)+1] + nums[-(i+1)+1]
        
        print(leftSum)
        print(rightSum)

        for i in range(len(leftSum)):
            ans.append(abs(leftSum[i]-rightSum[i]))
        
        print(ans)
        return ans