class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]

        max_candies = max(candies)

        for i in candies:
            if(i>=(max_candies-extraCandies)):
                ans.append(True)
            else:
                ans.append(False)
        
        print(ans)
        return ans