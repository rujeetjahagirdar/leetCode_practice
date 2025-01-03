class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        totalSum = sum(arr)

        if(totalSum%3 !=0):
            return False
        
        partitionSum = totalSum//3
        currentSum=0
        numberPartitions = 0

        for i in range(len(arr)):
            currentSum +=arr[i]

            if(currentSum==partitionSum):
                numberPartitions+=1
                currentSum=0

                if(numberPartitions==3):
                    return True
        return False