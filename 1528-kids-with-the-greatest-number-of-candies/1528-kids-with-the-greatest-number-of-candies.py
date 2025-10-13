class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]

        mx = max(candies)

        for i in candies:
            if(i+extraCandies >=mx):
                ans.append(True)
            else:
                ans.append(False)
        return ans