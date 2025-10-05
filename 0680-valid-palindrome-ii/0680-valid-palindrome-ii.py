class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalim(s):
            if(len(s)==1):
                return True
            return s[:]==s[::-1]

        l=0
        r=len(s)-1


        while(l<=r):
            if(s[l]==s[r]):
                l+=1
                r-=1
            elif(s[l]!=s[r]):
                if(checkPalim(s[l:r])):
                    return True
                if(checkPalim(s[l+1:r+1])):
                    return True
                return False
        return True