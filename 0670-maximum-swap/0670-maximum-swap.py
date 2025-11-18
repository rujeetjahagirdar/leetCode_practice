class Solution:
    def maximumSwap(self, num: int) -> int:
        
        #preprocess, keep track of max element till now from right to left
        #traverse from left to right, if max number available to right replace it
        
        numStr = [int(i) for i in list(str(num))]

        maxTill = [None]*len(numStr)
        mx = (numStr[-1], len(numStr)-1)

        for i in range(len(numStr)-1, -1, -1):
            if(numStr[i]>mx[0]):
                maxTill[i] = (numStr[i], i)
                mx = (numStr[i], i)
            else:
                maxTill[i] = mx
        
        for i in range(len(numStr)):
            if(maxTill[i][0]>numStr[i]):
                numStr[i], numStr[maxTill[i][1]] = numStr[maxTill[i][1]], numStr[i]
                break

        # print(numStr)
        ans=0

        for i in numStr:
            ans = ans*10+i
        return(ans)