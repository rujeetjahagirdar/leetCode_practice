# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         if(n==1):
#             if(k>3):
#                 return ''
#             return ['a','b','c'][k-1]

#         if(k>(3*(2**(n-1)))):
#             return ''
        
#         stack=[]
#         while(n>0):
#             if(n==1):
#                 if(k>3):
#                     return ''
#                 stack.append(['a','b','c'][k])
#                 break
#             if(n>1):
#                 i = (k-1)//(2**(n-1))
#                 if(not stack):
#                     if(i>2):
#                         return ''
#                     stack.append(['a','b','c'][i])
#                     k=(k-1)%(2**(n-1))+1
#                     print(k)
#                     print(stack)
#                 else:
#                     if(stack[-1]=='a'):
#                         if(i>=2):
#                             return ''
#                         stack.append(['b','c'][i])
#                         k=(k-1)%(2**(n-1))+1
#                         print(k)
#                         print(stack)
#                     elif(stack[-1]=='b'):
#                         if(i>=2):
#                             return ''
#                         stack.append(['a','c'][i])
#                         k=(k-1)%(2**(n-1))+1
#                         print(k)
#                         print(stack)
#                     elif(stack[-1]=='c'):
#                         if(i>=2):
#                             return ''
#                         stack.append(['a','b'][i])
#                         k=(k-1)%(2**(n-1))+1
#                         print(k)
#                         print(stack)
#             n-=1
#         print(stack)
#         return ''.join(stack)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Pre-calculate how many happy strings of length `n` start with a given char
        # dp[len][char] = number of happy strings of length `len` starting with `char`
        # For each position, decide whether to pick 'a', 'b', or 'c'

        # 1) If n=1, total = 3
        # 2) If n>1, at each step, we can't pick the previous char, so dp-based approach
        # or we can do a backtracking approach with skipping.

        from math import comb

        # total number of happy strings = 3 * 2^(n-1)
        total = 3 * (1 << (n - 1)) if n > 1 else 3
        if k > total:
            return ""

        # A function to count how many happy strings of length `length` start with char `prev`
        # We'll memoize to speed up.
        from functools import lru_cache

        @lru_cache(None)
        def count(length, prev):
            """Returns how many happy strings of length `length` can be formed if `prev` is the last chosen char 
            (or '' if we are at the start)."""
            if length == 0:
                return 1
            total_ = 0
            for c in "abc":
                if c != prev:
                    total_ += count(length - 1, c)
            return total_

        # Build the result string
        result = []
        prev = ''  # No previous char initially
        length = n
        curr_k = k

        for i in range(n):
            # For each position, try 'a','b','c' in lex order
            for c in "abc":
                if c == prev:
                    continue
                # If we pick c at position i, how many ways to build the rest?
                ways = count(n - i - 1, c)
                if curr_k <= ways:
                    result.append(c)
                    prev = c
                    break
                else:
                    curr_k -= ways
        
        return "".join(result)
