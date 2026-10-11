class Solution:
    def checkRecord(self, s: str) -> bool:
        
        # if(len(s)==2):
        #     if(s=='AA'):
        #         return False

        if(s.count('A')>=2):
            return False

        for i in range(len(s)-2):
            # if(s[i]=='A'):
            #     if(s[i+1]=='A'):
            #         return False
            if(s[i]=='L'):
                if(s[i+1]==s[i+2]=='L'):
                    return False
        
        return True