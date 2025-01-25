class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        allProduct =1

        for i in nums:
            if(i!=0):
                allProduct*=i
        
        ans=[]
        if(nums.count(0)==0):
            for i in nums:
                ans.append(allProduct//i)
        elif(nums.count(0)==1):
            for i in nums:
                if(i==0):
                    ans.append(allProduct)
                else:
                    ans.append(0)
        else:
            for i in nums:
                ans.append(0)
        
        print(ans)
        return ans
        