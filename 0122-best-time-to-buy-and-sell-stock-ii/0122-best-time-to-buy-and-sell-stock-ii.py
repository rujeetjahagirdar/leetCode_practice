class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0

        lastBuyPrice = prices[0]

        #[1,3,1,5,1]

        for i in range(1, len(prices)):
            if(prices[i]<=lastBuyPrice):
                lastBuyPrice = prices[i]
            else:
                profit = prices[i] - lastBuyPrice

                ans+=profit
                lastBuyPrice = prices[i]

        
        return ans