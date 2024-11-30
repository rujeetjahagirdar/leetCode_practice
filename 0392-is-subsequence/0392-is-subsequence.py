class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        ans=False
        while(j<len(t) and i<len(s)):
            if(s[i]==t[j]):
                i+=1
                j+=1
                ans=True
            else:
                j+=1

        if(i>=len(s)):
            return True
        return False