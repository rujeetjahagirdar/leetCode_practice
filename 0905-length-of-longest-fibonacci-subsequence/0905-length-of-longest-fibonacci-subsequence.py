# class Solution:
#     def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
#         def findFibSeq(l, r, arr):
#             if(not arr or l+r not in arr):
#                 return 0
            
#             return 1+findFibSeq(r, l+r, arr[arr.index(l+r):])
        

#         # l=arr[0]
#         # r=arr[1]
#         ans = float('-inf')


#         for i in range(len(arr)-1):
#             for j in range(i+1, len(arr)):
#                 l=arr[i]
#                 r=arr[j]
#                 if(l+r in arr):
#                     tAns=2
#                 else:
#                     tAns=0
#                 tAns += findFibSeq(l, r, arr[arr.index(r):])
#                 ans=max(ans, tAns)
        
#         print(ans)
#         return ans
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0  # can't have a fib-like subsequence of length < 3
        
        # 1. Build a dictionary to quickly get the index of a given value
        index_map = {}
        for i, val in enumerate(arr):
            index_map[val] = i
        
        # 2. Initialize DP table
        # dp[i][j] = length of the longest fib-like subsequence ending with arr[i], arr[j]
        # By default, any pair has length 2 (just those two numbers)
        dp = [[2] * n for _ in range(n)]
        
        ans = 0
        
        # 3. Fill the DP table
        for j in range(n):
            for i in range(j):
                # The "previous" number we'd want is arr[j] - arr[i]
                needed = arr[j] - arr[i]
                
                # We also require needed < arr[i] because arr is strictly increasing
                # so for a valid fib step: arr[k], arr[i], arr[j] => arr[k] + arr[i] = arr[j].
                # If needed >= arr[i], it's not a valid step in this array's strictly increasing order.
                if needed < arr[i] and needed in index_map:
                    k = index_map[needed]
                    dp[i][j] = dp[k][i] + 1  # extend the sequence
                else:
                    dp[i][j] = 2  # no valid "previous," so length is just 2
                ans = max(ans, dp[i][j])
        
        # 4. If we never found a sequence of length >= 3, return 0
        return ans if ans >= 3 else 0
