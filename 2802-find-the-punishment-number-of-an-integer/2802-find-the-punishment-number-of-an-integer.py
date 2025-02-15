class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def canPartition(numberS, target):
            #1296
            numberS = str(numberS)
            # print(numberS, target)

            if(target<0):
                return False

            if(int(numberS)<target):
                return False
            
            if(int(numberS)==target):
                return True

            
            
            for i in range(len(numberS)):
                left = numberS[:i+1] #1
                right = numberS[i+1:] #296
                #1 296
                if(canPartition(right, target - int(left))):
                    return True
        


        ans=0
        for i in range(1, n+1):
            if(canPartition(i*i, i)):
                ans+=i*i
        
        print(ans)
        return ans