class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            t = ''
            for i in range(len(s)-1):
                t+=(str((int(s[i])+int(s[i+1]))%10))
                print(t)
            s=t
        
        return s[0]==s[1]