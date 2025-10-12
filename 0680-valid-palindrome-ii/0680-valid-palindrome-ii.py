class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalim(t):
            return t==t[::-1]

        # k=1

        l=0
        r = len(s)-1

        while(l<r):
            if(s[l]==s[r]):
                l+=1
                r-=1
            else:
                if(checkPalim(s[l:r])):
                    return True
                if(checkPalim(s[l+1:r+1])):
                    return True
                return False
        return True