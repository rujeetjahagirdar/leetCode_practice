class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minPrice=float('inf')
        for i in prices:
            if(i<minPrice):
                minPrice=i
            elif (i-minPrice>=profit):
                profit = i -minPrice
        return profit