class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[0]*len(prices)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[j]<=prices[i]):
                    ans[i] = prices[i]-prices[j]
                    break
                ans[i] = prices[i]
        ans[-1] = prices[-1]
        print(ans)
        return ans