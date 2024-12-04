class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=0
        j=0

        

        while(i<len(str2)):
            while(j<len(str1) and (ord(str2[i]) - ord(str1[j]) + 26) % 26 not in (0,1)):
                j+=1
            
            if(j>=len(str1)):
                return False
            else:
                # if(i==len(str2)-1):
                #     return True
                i+=1
            j+=1
        return True