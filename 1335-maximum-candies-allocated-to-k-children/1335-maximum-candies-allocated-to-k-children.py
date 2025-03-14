class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if(sum(candies)<k):
            return 0
            
        def check(candies, x):
            kprime=0

            for i in candies:
                kprime+=(i//x)
            return kprime
        
        l=1
        r=max(candies)
        best = 0

        while(l<=r):
            mid = l +(r-l) //2

            ans = check(candies, mid) 
            # if(ans==k):
            #     return mid
            if(ans>=k):
                best=mid
                l=mid+1
            else:
                r=mid-1
        
        return best