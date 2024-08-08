class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax=[]
        lm=0
        rightMax=[]
        rm=0
        for i in range(0,len(height)):
            leftMax.append(lm)
            rightMax.append(rm)
            if(height[i]>lm):
                lm=height[i]
            if(height[::-1][i]>rm):
                rm=height[::-1][i]
        rightMax = rightMax[::-1]

            
        
        ans=0
        for i in range(1,len(height)-1):
            # capacity  = min(max(height[:i]), max(height[i+1:])) - height[i]
            capacity  = min(leftMax[i], rightMax[i]) - height[i]
            # print(i, capacity)
            if capacity > 0:
                ans = ans + capacity
                # print("ans= ",ans)
                
        return(ans)