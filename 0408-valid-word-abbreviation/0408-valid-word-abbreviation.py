class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        n=0

        if(abbr.isnumeric()):
            if(len(word)!=int(abbr)):
                return False
        
        while(j<len(abbr) and i<len(word)):
            if(abbr[j].isnumeric()):
                if(n==0 and int(abbr[j])==0):
                    return False
                n=(10*n+int(abbr[j]))
            
            elif(abbr[j].isalpha()):
                i+=n
                n=0
                if(i>=len(word) or word[i]!=abbr[j]):
                    return False
                i+=1
            
            j+=1
        
        if(i+n==len(word) and j==len(abbr)):
            return True
        else:
            return False
            