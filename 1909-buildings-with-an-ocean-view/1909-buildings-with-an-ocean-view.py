class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans=[]

        mxTillNow = 0

        for i in range(len(heights)-1, -1, -1):
            if(heights[i]>mxTillNow):
                ans.append(i)
            mxTillNow = max(mxTillNow, heights[i])

        return ans[::-1]