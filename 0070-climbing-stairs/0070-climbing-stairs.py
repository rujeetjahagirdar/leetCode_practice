class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1]
        for i in range(n-1):
            dp.append(dp[-1]+dp[-2])
        print(dp)
        return dp[-1]