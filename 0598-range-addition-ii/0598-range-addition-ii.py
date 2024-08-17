class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return m*n
        n1 = sorted(ops, key=lambda x:x[0])[0][0]
        n2 = sorted(ops, key=lambda x:x[1])[0][1]
        return n1*n2