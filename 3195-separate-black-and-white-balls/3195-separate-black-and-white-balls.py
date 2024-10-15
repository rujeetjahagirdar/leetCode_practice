class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        l = r = 0
        
        while(r<len(s)):
            if(s[r]=='0'):
                ans +=(r-l)
                l+=1
            r+=1
        print(ans)
        return ans