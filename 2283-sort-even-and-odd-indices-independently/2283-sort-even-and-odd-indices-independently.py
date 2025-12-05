class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        evenNums = []
        oddNums = []

        for i in range(len(nums)):
            if(i%2==0):
                evenNums.append(nums[i])
            else:
                oddNums.append(nums[i])
        
        evenNums.sort()
        oddNums.sort(reverse=True)

        ans=[]
        for i in range(len(nums)):
            if(i%2==0):
                ans.append(evenNums.pop(0))
            else:
                ans.append(oddNums.pop(0))
        
        return(ans)