class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0

        lowestBuy = prices[0]

        for i in range(len(prices)):
            if(prices[i]<lowestBuy):
                lowestBuy = prices[i]
            else:
                profit = prices[i] - lowestBuy
                ans = max(ans, profit)
        return ans