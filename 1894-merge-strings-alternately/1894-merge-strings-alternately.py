class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ln = max(len(word1), len(word2))

        ans=''

        for i in range(ln):
            if(i<len(word1)):
                ans+=word1[i]
            else:
                pass
            if(i<len(word2)):
                ans+=word2[i]
            else:
                pass
            
        return(ans)