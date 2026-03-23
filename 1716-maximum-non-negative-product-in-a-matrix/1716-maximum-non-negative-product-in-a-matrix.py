class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
            #DP,
            #for any cell i,j max product at i,j, will be max of curr * upper cell, curr * left cell
            # but since two negative values can create prositive product, we need keep track of negative products as well
            #for every cell (i, j), keep track of max product, min_product 
            m, n = len(grid), len(grid[0])
            MOD = 10**9 + 7
            max_product_dp = [[0]*n for _ in range(m)]
            min_product_dp = [[0]*n for _ in range(m)]

            max_product_dp[0][0] = min_product_dp[0][0] = grid[0][0]

            
            #for first col
            for i in range(1, m):
                max_product_dp[i][0] = max_product_dp[i-1][0] * grid[i][0]
                min_product_dp[i][0] = min_product_dp[i-1][0] * grid[i][0]
            
            #for first row
            for j in range(1, n):
                max_product_dp[0][j] = max_product_dp[0][j-1] * grid[0][j]
                min_product_dp[0][j] = min_product_dp[0][j-1] * grid[0][j]
            
            #for rest of the cells
            for i in range(1, m):
                for j in range(1, n):
                    possible_products = [
                        max_product_dp[i][j-1] * grid[i][j],
                        max_product_dp[i-1][j] * grid[i][j],
                        min_product_dp[i][j-1] * grid[i][j],
                        min_product_dp[i-1][j] * grid[i][j]
                        
                    ]

                    max_product_dp[i][j] = max(possible_products)
                    min_product_dp[i][j] = min(possible_products)
            
            ans = max_product_dp[m-1][n-1]
            print(ans)

            if(ans>=0):
                return ans % MOD
            return -1
        
        ############################
        
        # # dfs with backtracking

        # directions = [(1,0), (0, 1)]
        # visited = set()
        # ans=-1
        # MOD = pow(10, 9) + 7

        # def dfs(i, j, cummProd):
        #     nonlocal ans

        #     if((i, j)==(len(grid)-1, len(grid[0])-1)):
        #         cummProd *=grid[i][j]
        #         if(cummProd>=0):
        #             ans = max(ans, cummProd)
        #         return
            
        #     cummProd *=grid[i][j]
            
        #     for direction in directions:
        #         newi, newj = i+direction[0], j+direction[1]
        #         if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and (newi, newj) not in visited):
        #             visited.add((newi, newj))
        #             dfs(newi, newj, cummProd)
            
        #             visited.remove((newi, newj))

        # dfs(0,0, 1)

        # # print(ans)
        # if(ans>0):
        #     return ans % MOD
        # return ans