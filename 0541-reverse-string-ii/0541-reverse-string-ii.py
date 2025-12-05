class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''

        if(len(s)<=k):
            return s[::-1]

        for i in range(0, len(s), 2*k):
            # print(s[i:i+k])
            # print(s[i+k: i+k+k])
            ans+=s[i:i+k][::-1]+s[i+k:i+k+k]
            print(ans)
        
        # if(i>=len(s)-(2*k)):
        #     ans+=s[i:len(s)][::-1]
        
        return(ans)