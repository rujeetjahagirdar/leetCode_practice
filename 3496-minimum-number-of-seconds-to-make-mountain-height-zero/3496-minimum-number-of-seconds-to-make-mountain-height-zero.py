class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # binary search on Time

        def can_finish(t):
            height_reduced=0
            for i in workerTimes:
                k = (2*t)//i
                height_reduced+=int((sqrt(1+4*k)-1) / 2)
            
            if(height_reduced>=mountainHeight):
                return True
            return False

        l = 1
        r = min(workerTimes) * mountainHeight * (mountainHeight+1) //2

        while(l<r):
            mid = (l+r)//2

            if(can_finish(mid)):
                r = mid
            else:
                l=mid+1
            
        return l