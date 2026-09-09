class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n)) #length of n

        ans=0

        if(l<=3):
            return 0
        
        for i in range(4, l):
            ans+= 9 * pow(10, i-1)
        
        ans+= (n - pow(10, l-1)) + 1

        return(ans)