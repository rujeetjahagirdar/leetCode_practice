class Solution:
    def maxScore(self, s: str) -> int:
        ans=float("-inf")
        zeroCount = 0
        oneCount = 0

        for i in s:
            if(i=='1'):
                oneCount+=1
        
        for i in range(len(s)-1):
            if(s[i]=='1'):
                oneCount-=1
            elif(s[i]=='0'):
                zeroCount+=1
            ans = max(ans, zeroCount+oneCount)
        
        print(ans)
        return ans