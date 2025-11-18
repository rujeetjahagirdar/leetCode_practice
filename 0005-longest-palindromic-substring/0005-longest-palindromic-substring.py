class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #expand from center,
        #two cases, string with even length
                    #string with odd length

        ans=s[0]

        # if(len(s)==1):
        #     return s
        
        # if(len(s)==2):
        #     if(s[0]==s[1]):
        #         return s
        #     else:
        #         return s[0]

        #odd length
        i=0
        while(i<len(s)):
            l=i-1
            r=i+1

            while(l>=0 and r<len(s) and s[l]==s[r]):
                if((r-l +1)>len(ans)):
                    ans=s[l:r+1]
                l-=1
                r+=1
            i+=1
        print(ans)

        #even length
        i=0
        while(i<len(s)-1):
            j=i+1

            l=i
            r=j

            while(l>=0 and r<len(s) and s[l]==s[r]):
                if((r-l +1)>len(ans)):
                    ans=s[l:r+1]
                l-=1
                r+=1
            i+=1
        print(ans)

        return ans