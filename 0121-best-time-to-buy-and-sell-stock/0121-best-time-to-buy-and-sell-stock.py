class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        ans = 0

        for i in prices:
            if(i>buyPrice):
                ans=max(ans, (i-buyPrice))
            elif(i<buyPrice):
                buyPrice=i
        
        print(ans)
        return ans