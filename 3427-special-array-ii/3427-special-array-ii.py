class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        # def checkParity(arr):
        #     # print(arr)
        #     if(len(arr)==1):
        #         return True
        #     elif(len(arr)==2):
        #         if(arr[0]%2==0 and arr[1]%2!=0):
        #             return True
        #         elif(arr[1]%2==0 and arr[0]%2!=0):
        #             return True
        #         else:
        #             return False
        #     for i in range(1,len(arr)-1):
        #         if(arr[i]%2==0):
        #             if(arr[i-1]%2==0 or arr[i+1]%2==0):
        #                 return False
        #         else:
        #             if(arr[i-1]%2!=0 or arr[i+1]%2!=0):
        #                 return False
        #     return True
        

        # ans=[]
        # for q in queries:
        #     if(checkParity(nums[q[0]:q[1]+1])):
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # print(ans)
        # return ans
        ##########################################

       #Pre-computation to check maxReach from every element 
        #[1,2,3,4,5,6,7,7,8,9,10]
        # maxReachArr = [-1]*len(nums)
        # j=0
        # for i in range(len(nums)):
        #     # j=i+1
        #     j=max(j, i)
        #     while(j<len(nums)-1 and nums[j]%2!=nums[j+1]%2):
        #         j+=1
        #     maxReachArr[i]=j
        # print(maxReachArr)

        i=0
        j=0
        maxReachArr = []
        while(i<len(nums)):
            while(j<len(nums)-1 and nums[j]%2!=nums[j+1]%2):
                j+=1
            maxReachArr.extend([j]*(j-i+1)) #when parity breaks, all the elements from i to j (parity breaking point) will have valid parity, so we can skip the i to j+1 (parity breaking point +1)
            i=j+1
            j+=1
            # print(maxReachArr)
        ans=[]

        for q in queries:
            if(q[1]<=maxReachArr[q[0]]):
                ans.append(True)
            else:
                ans.append(False)
        print(ans)
        return ans