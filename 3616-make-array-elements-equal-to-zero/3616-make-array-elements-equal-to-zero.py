class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        totalSum = sum(nums)
        prefixSum = [-1]*len(nums) #excluding self
        cSum=0
        for i in range(len(nums)):
            prefixSum[i]=cSum
            cSum+=nums[i]
        
        ans=0

        for i in range(len(nums)):
            if(nums[i]==0):
                rightSum = totalSum - prefixSum[i]
                if(prefixSum[i]==rightSum):
                    ans+=2*1
                elif(abs(rightSum-prefixSum[i])==1):
                    ans+=1
        
        return ans

        ###################################
        # leftSum = [0]*len(nums)
        # rightSum = [0]*len(nums)

        # cSum=0
        # for i in range(len(nums)):
        #     leftSum[i]=cSum
        #     cSum+=nums[i]

        # print(leftSum)

        # cSum=0
        # for i in range(len(nums)-1, -1, -1):
        #     rightSum[i]=cSum
        #     cSum+=nums[i]
        # print(rightSum)

        # ans = []

        # for i in range(len(leftSum)):
        #     if(nums[i]==0):
        #         if(leftSum[i]==rightSum[i]):
        #             ans.append(i)
        #             ans.append(i)
        #         elif(abs(leftSum[i]-rightSum[i])==1):
        #             ans.append(i)
        
        # print(ans)
        # return len(ans)