class Solution:
    def checkValidString(self, s: str) -> bool:
        openBrackstes = []
        stars = []

        for i in range(len(s)):
            if(s[i]=='('):
                openBrackstes.append(i)
            elif(s[i]=='*'):
                stars.append(i)
            else:
                if(openBrackstes):
                    openBrackstes.pop()
                elif(stars):
                    stars.pop()
                else:
                    return False
        
        while(openBrackstes and stars):
            if(stars[-1]>openBrackstes[-1]):
                openBrackstes.pop()
                stars.pop()
            else:
                return False
        if(openBrackstes):
            return False
        
        return True