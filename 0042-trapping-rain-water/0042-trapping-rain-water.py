class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = []
        # leftMax.append(0)

        lmax = 0

        for i in range(len(height)):
            leftMax.append(lmax)
            lmax = max(lmax, height[i])
        
        print(leftMax)

        rightMax=[]
        rmax=0
        for i in reversed(range(len(height))):
            rightMax.append(rmax)
            rmax = max(rmax, height[i])
        rightMax = rightMax[::-1]
        print(rightMax)

        ans=0

        for i in range(len(height)):
            area = min(leftMax[i], rightMax[i])-height[i]
            # print(area)
            if(area>0):
                ans+=area
        
        print(ans)
        return ans