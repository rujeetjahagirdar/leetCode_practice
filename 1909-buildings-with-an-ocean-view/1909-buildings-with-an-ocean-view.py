class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        #TC: O(n)
        #SC: O(n)

        ans=[]

        mxTill = 0

        for i in range(len(heights)-1, -1, -1):
            if(heights[i]>mxTill):
                ans.append(i)
                mxTill = heights[i]
        
        return ans[::-1]