class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        while(i<len(s) and j<len(t)):
            if(s[i]==t[j]):
                i=i+1
            j=j+1
        return i==len(s)