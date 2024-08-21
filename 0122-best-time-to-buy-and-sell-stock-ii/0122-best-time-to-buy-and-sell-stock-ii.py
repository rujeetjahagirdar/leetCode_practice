class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==sorted(prices, reverse=True):
            return 0
        elif prices == sorted(prices):
            return prices[-1]-prices[0]
        else:
            profit = 0
            for i in range(len(prices)-1):
                if(prices[i+1]>prices[i]):
                    profit +=prices[i+1] - prices[i]
            print(profit)
            return profit