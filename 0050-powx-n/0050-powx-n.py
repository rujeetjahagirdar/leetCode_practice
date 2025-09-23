class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ans=1

        if(n<0):
            n = -1*n
            x = (1.0/x)
        
        while(n!=0):
            if(n%2==1):
                ans*=x
                n-=1
            else:
                x*=x
                n=n//2
        print(ans)
        return ans