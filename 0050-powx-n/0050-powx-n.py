class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1

        if(n<0):
            x = (1/x)
            n= -1 * n

        while(n>0):
            if(n%2!=0): #n is odd
                ans= ans * x
                n=n-1
            else:       #n is even
                x = x*x
                n=n//2
        
        return(ans)
