class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flipCount=0
        binA = str(bin(a)[2:])
        binB = str(bin(b)[2:])
        binC = str(bin(c)[2:])
        mxLen = max(len(binA), len(binB), len(binC))
        binA = binA.rjust(mxLen, '0')
        binB = binB.rjust(mxLen, '0')
        binC = binC.rjust(mxLen, '0')
        for i in range(len(binC))[::-1]:
            if(binC[i]=='1'):
                if(binB[i]=='0' and binA[i]=='0'):
                    flipCount=flipCount+1
            elif(binC[i]=='0'):
                if(binB[i]=='1' and binA[i]=='1'):
                    flipCount = flipCount + 2
                elif(binB[i]=='1' and binA[i]=='0'):
                    flipCount=flipCount+1
                elif(binB[i]=='0' and binA[i]=='1'):
                    flipCount=flipCount+1
        print(flipCount)
        return flipCount