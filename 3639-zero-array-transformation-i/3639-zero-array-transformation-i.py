class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        newArray = [0] * (len(nums)+1)

        for l, r in queries:
            newArray[l] +=1
            newArray[r+1] -=1

        for i in range(1, len(newArray)):
            newArray[i] +=newArray[i-1]
        
        print(newArray)

        for i in range(len(nums)):
            if(newArray[i]<nums[i]):
                return False
        
        return True