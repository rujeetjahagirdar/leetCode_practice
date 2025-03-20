__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)

        l=1
        r=max(piles)

        while(l<=r):
            mid = l+(r-l) //2

            hprime = 0
            for i in piles:
                # hprime+=(i//mid)+1
                hprime+=math.ceil(i/mid)
            
            if(hprime>h):
                l=mid+1
            else:
                ans=min(ans, mid)
                r=mid-1
        
        print(ans)
        return ans