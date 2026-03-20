class Solution:
    def numSub(self, s: str) -> int:
        
        # #sliding window

        # l=0
        # ans=0
        # MOD = 10**9 + 7

        # for r in range(len(s)):
        #     if(s[r]=='1'):
        #         ans+=(r - l +1)
        #     else:
        #         l = r+1
        
        # return ans % MOD

        #########

        #stack

        stack = []
        ans=0
        MOD = 10**9 + 7

        for i in range(len(s)):
            if(s[i]=='1'):
                stack.append('1')
            else:
                if(stack):
                    ans+= (len(stack) * (len(stack)+1) //2)
                    stack=[]
        if(stack):
            ans+= (len(stack) * (len(stack)+1) //2)
            stack=[]
        
        return ans % MOD