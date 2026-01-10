class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if(not str1 or not str2):
            return ''
        
        if(str1+str2 != str2+str1):
            return ''

        if(len(str1)<len(str2)):
            s = str1
        else:
            s = str2
        
        def checkDivisor(t):
            print(t)
            if(len(str1)%len(t)==0 and len(str2)%len(t)==0):
                if(t*(len(str1)//len(t))==str1 and t*(len(str2)//len(t))==str2):
                    return True
                else:
                    return False
            else:
                return False
        

        print(s)
        for i in range(len(s)-1, -1, -1):
            if(checkDivisor(s[:i+1])):
                return s[:i+1]
        return ''
