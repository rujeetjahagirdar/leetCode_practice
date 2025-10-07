class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxTill = heights[-1]
        ans = [len(heights)-1]

        for i in range(len(heights)-2, -1, -1):
            if(heights[i]>maxTill):
                ans.append(i)
                maxTill = max(maxTill, heights[i])
        return(ans[::-1])