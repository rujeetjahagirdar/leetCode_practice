class Solution:
    def kthCharacter(self, k: int) -> str:
        s='a'
        while(len(s)<k):
            s1=''
            for i in range(len(s)):
                if(s[i]=='z'):
                    s1+='a'
                else:
                    s1+=chr(ord(s[i])+1)
            s+=s1
        print(s)
        return(s[k-1])