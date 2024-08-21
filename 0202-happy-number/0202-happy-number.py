class Solution:
    def isHappy(self, n: int) -> bool:
        ans =  n
        seen = set()
        while True:
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sum([int(i)**2 for i in str(n)])
            # seen.add(n)
            # print(seen)