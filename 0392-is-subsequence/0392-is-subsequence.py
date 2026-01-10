class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(not t and not s):
            return True
        if(not t):
            return False
        if(len(t)<len(s)):
            return False
        if(len(s)==len(t)):
            return s==t
        if(not s and t):
            return True
        
        p1=0
        p2=0

        while(p2<len(t) and p1<len(s)):
            if(t[p2]==s[p1]):
                p1+=1
            p2+=1
        
        if(p1==len(s)):
            return True
        return False