class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashM = {}
        ans=0

        for i in range(len(t)):
            hashM[t[i]]=i
        
        for i in range(len(s)):
            ans+=abs(i-hashM[s[i]])
        
        return ans