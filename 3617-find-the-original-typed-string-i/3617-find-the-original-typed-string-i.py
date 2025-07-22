class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1

        l=0
        
        while(l<len(word)):
            r=l
            while(r<len(word) and (word[r]==word[l])):
                r+=1

            if(r-l)>1:
                ans+=(r-l)-1
            l=r
        
        print(ans)
        return ans
