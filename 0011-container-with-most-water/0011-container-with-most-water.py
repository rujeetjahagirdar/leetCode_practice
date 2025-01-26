class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=float("-inf")

        l = 0
        r = len(height)-1

        while(l<r):
            area = (r-l)*min(height[r],height[l])
            ans=max(ans, area)

            if(height[l]<height[r]):
                l+=1
            elif(height[l]>=height[r]):
                r-=1
        
        return ans