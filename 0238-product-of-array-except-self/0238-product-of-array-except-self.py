class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=[]
        # dp=[[1]*len(nums) for i in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if(i==j):
        #             dp[i][j]=nums[j]
        #         else:
        #             dp[i][j]=dp[i][j-1]*nums[j]
        # # print(dp)
        # for i in range(len(nums)):
        #     if(i==0):
        #         ans.append(dp[i+1][len(nums)-1])
        #     elif (i==len(nums)-1):
        #         ans.append(dp[0][len(nums)-2])
        #     else:
        #         ans.append((dp[0][i-1])*(dp[i+1][len(nums)-1]))
        # return(ans)
###########-----------------------------------------#####################
        # leftMult=[1]*len(nums)
        # rightMult=[1]*len(nums)
        # cumMult=1
        # for i in range(1,len(nums)):
        #     cumMult=cumMult*nums[i-1]
        #     leftMult[i]=cumMult
        # # print(leftMult)
        # cumMult=1
        # nums=nums[::-1]
        # for i in range(1,len(nums)):
        #     cumMult=cumMult*nums[i-1]
        #     rightMult[i]=cumMult
        # # print(rightMult[::-1])
        # return ([(leftMult[i]*rightMult[::-1][i]) for i in range(len(leftMult))])
##################-------------------------------------------###################################
        '''''''''
        Used a hashMap to count the frequency if each number in nums.
        Calculated multiplication of all numbers by traversing the hashMap. If number zero exists for one time then use one instead zero during multiplication.
        Traversed nums array and calculated ans array by dividing all multiplication by the current element.
        '''
        hashM={}
        for i in nums:
            if(i not in hashM):
                hashM[i]=1
            else:
                hashM[i]=hashM[i]+1
        allMult=1
        for n in hashM:
            if(n==0 and hashM[n]==1):
                allMult = allMult * pow(1,hashM[n])
            else:
                allMult = allMult * pow(n,hashM[n])
            # print(allMult)
        # print(hashM)
        # print(allMult)
        ans=[0]*len(nums)
        if(0 in hashM):
            if(hashM[0]==1):
                ans[nums.index(0)]=allMult
                return (ans)
            elif(hashM[0]>1):
                return ans
        else:
            for i in range(len(nums)):
                ans[i]=allMult//nums[i]
            return ans
