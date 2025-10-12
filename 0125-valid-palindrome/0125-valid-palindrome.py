class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r = len(s)-1

        if(len(s)==1):
            return True

        while(l<r):
            if(not s[l].isalnum()):
                l+=1
                continue
            if(not s[r].isalnum()):
                r-=1
                continue
            if(s[l].lower()==s[r].lower()):
                l+=1
                r-=1
            else:
                return False
        return True