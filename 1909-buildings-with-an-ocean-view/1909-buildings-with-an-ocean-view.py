class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # prefixArr = [0]*(len(heights)+1)
        # heights = heights[::-1]
        # mxHeight = heights[0]
        # for i in range(1,len(heights)):
        #     prefixArr[i+1] = mxHeight
        #     mxHeight = max(mxHeight, heights[i])
        # heights=heights[::-1]
        # prefixArr=prefixArr[::-1]
        # print(heights[::-1])
        # print(prefixArr[::-1])
        # ans=[]

        # for i in range(len(heights)):
        #     if(heights[i]>prefixArr[i]):
        #         ans.append(i)
        # print(ans)
        # return ans
        ########################
        ans=[]

        mxHeight = 0

        for i in reversed(range(len(heights))):
            # print(heights[i])
            if(heights[i]>mxHeight):
                ans.append(i)
                mxHeight = max(mxHeight, heights[i])
        print(ans[::-1])
        return ans[::-1]