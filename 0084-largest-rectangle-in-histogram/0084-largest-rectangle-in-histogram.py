class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        mxArea = 0

        for i in range(len(heights)):
            while(stack[-1]!=-1 and heights[stack[-1]]>=heights[i]):
                idx = stack.pop()
                h = heights[idx]
                width = i - stack[-1] -1
                mxArea = max(mxArea, h*width)
            
            stack.append(i)
            # print(stack)
        
        # while(stack[-1]!=-1):
        while(stack[-1]!=-1):
            idx = stack.pop()
            h = heights[idx]
            width = len(heights) - stack[-1] -1
            mxArea = max(mxArea, h*width)
        # print(stack)

        # print(mxArea)
        return(mxArea)