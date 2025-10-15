class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalim(t):
            # return t==t[::-1]
            l=0
            r = len(t)-1

            while(l<r):
                if(t[l]!=t[r]):
                    return False
                l+=1
                r-=1
            return True

        # k=1

        l=0
        r = len(s)-1

        while(l<r):
            if(s[l]==s[r]):
                l+=1
                r-=1
            else:
                if(checkPalim(s[l:r])): #remove r char
                    return True
                if(checkPalim(s[l+1:r+1])): #remove l char
                    return True
                return False
        return True