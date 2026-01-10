class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=0
        windowVowels=0
        l=r=0

        while(r<len(s)):
            if(s[r] in 'aeiou'):
                windowVowels+=1
            
            while((r-l)>=k):
                if(s[l] in 'aeiou'):
                    windowVowels-=1
                l+=1
            
            ans=max(ans, windowVowels)

            r+=1
        

        print(ans)
        return ans