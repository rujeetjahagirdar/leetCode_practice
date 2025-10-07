class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        mxCandies = max(candies)

        for i in candies:
            if(i+extraCandies>=(mxCandies)):
                ans.append(True)
            else:
                ans.append(False)
        return ans