class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        prevBuy = prices[0]

        for i in range(len(prices)):
            if(prices[i]>prevBuy):
                ans+=(prices[i]-prevBuy)
                prevBuy = max(prevBuy, prices[i])
            else:
                prevBuy = prices[i]
        return(ans)