class Solution:
    def myAtoi(self, s: str) -> int:
        sign=None
        n=0

        i=0
        while(i<len(s) and s[i]==' '):
            i+=1
        
        if(i<len(s) and s[i]=='-'):
            sign='-'
            i+=1
        elif(i<len(s) and s[i]=='+'):
            sign='+'
            i+=1
        while(i<len(s) and s[i].isnumeric()):
            n = n*10+int(s[i])
            i+=1
        
        if(sign=='-'):
            n = -1*n
            return max(-2**31, n)
        
        return min(n, 2**31 -1)