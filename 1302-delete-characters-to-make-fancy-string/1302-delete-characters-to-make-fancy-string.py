class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=''

        
        i=0

        while(i<len(s)):
            if((i+1<len(s) and i+2<len(s)) and (s[i]==s[i+1]==s[i+2])):
                j=i+3
                while(j<len(s) and s[j]==s[i]):
                    j+=1
                ans+=s[i]
                ans+=s[i+1]
                i=j
            else:
                ans+=s[i]
                i+=1
            # print(ans)
        return ans