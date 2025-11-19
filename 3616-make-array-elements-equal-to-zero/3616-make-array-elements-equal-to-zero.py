class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        leftSum = [0]*len(nums)
        rightSum = [0]*len(nums)

        cSum=0
        for i in range(len(nums)):
            leftSum[i]=cSum
            cSum+=nums[i]

        print(leftSum)

        cSum=0
        for i in range(len(nums)-1, -1, -1):
            rightSum[i]=cSum
            cSum+=nums[i]
        print(rightSum)

        ans = []

        for i in range(len(leftSum)):
            if(nums[i]==0):
                if(leftSum[i]==rightSum[i]):
                    ans.append(i)
                    ans.append(i)
                elif(abs(leftSum[i]-rightSum[i])==1):
                    ans.append(i)
        
        print(ans)
        return len(ans)