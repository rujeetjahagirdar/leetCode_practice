class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #two pointer

        ans=0

        l=0
        r = len(height)-1

        while(l<r):
            area = min(height[l], height[r])* (r-l)
            ans = max(ans, area)

            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
        
        return(ans)