class Solution:
    def validPalindrome(self, s: str) -> bool:
        #abbxa
        def checkPalin(substr):
            return substr==substr[::-1]

        i=0
        j=len(s)-1

        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                # if(checkPalin(s[i:j])):
                #     return True
                # elif(checkPalin(s[i+1:j+1])):
                #     return True
                # else:
                #     return False
                return checkPalin(s[i:j]) or checkPalin(s[i+1:j+1])
        return True