class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        # sign = 
        if(x<0):
            sign = -1
        else:
            sign = 1
        
        x = abs(x)
        while x>0:
            n = x%10
            rev = rev*10 + n
            x = x//10
        
        print(rev)
        if(pow(-2, 31)<=rev<=pow(2, 31)-1):
            return sign*rev
        return 0