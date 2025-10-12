class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        n=0

        if(len(word)<len(abbr)):
            return False

        while(i<len(word) and j<len(abbr)):
            if(abbr[j].isalpha()):
                if(n>0):
                    i+=n
                    if(i>=len(word) or word[i]!=abbr[j]):
                        return False
                    n=0
                    i+=1
                else:
                    if(word[i]==abbr[j]):
                        i+=1
                    else:
                        return False
            elif(abbr[j].isnumeric()):
                if(n==0 and abbr[j]=='0'):
                    return False
                else:
                    n = n*10 + int(abbr[j])
            j+=1
        if(n>0):
            i+=n
            n=0

        if(i==len(word) and j==len(abbr)):
            return True
        return False