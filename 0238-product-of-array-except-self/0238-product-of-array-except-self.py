class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount=0
        totalProduct=1

        for i in nums:
            if(i!=0):
                totalProduct*=i
            else:
                zeroCount+=1
        
        ans=[]

        for i in range(len(nums)):
            if(nums[i]==0):
                if(zeroCount>1):
                    ans.append(0)
                else:
                    ans.append(totalProduct)
            else:
                if(zeroCount>0):
                    ans.append(0)
                else:
                    ans.append(totalProduct//nums[i])
        
        print(ans)
        return ans