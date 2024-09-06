class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        # cost = cost[::-1]
        for i in range(len(cost)-3, -1, -1):
            # print(dp, cost[i], i)
            dp[i]= min(cost[i]+dp[i+1], cost[i]+dp[i+2])
        print(dp)
        return min(dp[0], dp[1])