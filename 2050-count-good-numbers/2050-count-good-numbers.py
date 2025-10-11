class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #_ _ _ _ _

        def pown(n, m):
            ans=1
            while(m>0):
                if(m%2!=0):
                    ans = (ans*n)% (10**9 + 7)
                    m=m-1
                else:
                    n = (n**2)% (10**9 + 7)
                    m=m//2
                # print(ans, n, m)
            # ans = ans*n

            return(ans)



        if(n==1):
            return 5

        if(n%2==0):
            evenPlaces = n//2
        else:
            evenPlaces = n//2 +1
        
        return (pown(5,evenPlaces) * pown(4,(n-evenPlaces)))% (10**9 + 7)
