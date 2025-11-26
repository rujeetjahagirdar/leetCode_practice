class Solution:
    def isNumber(self, s: str) -> bool:
        
        seenDigit = False
        seenDot = False
        seenExponent = False
        seenSign = False

        for i in range(len(s)):
            if(s[i].isdigit()):
                seenDigit = True
            elif(s[i] in ['+','-']):
                #sign should be either at first or immediately after exponent
                if(i>0 and s[i-1] not in ('e','E')):
                    return False
                seenSign=True
            elif(s[i] in ('e','E')):
                #exponent must come after digit
                #must have only one exponent
                if(not seenDigit or seenExponent):
                    return False
                seenExponent = True
                seenDigit = False
            elif(s[i]=='.'):
                #only one dot
                #can not have dot after anytime exponent 
                if(seenDot or seenExponent):
                    return False
                seenDot = True
            
            else:
                #everything else, return False
                return False
        
        return seenDigit