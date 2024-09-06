class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # ans = 0

        ans = ''
        for i in s:
            ans+=str((ord(i)-ord('a'))+1)
        print(ans)
        for _ in range(k):
            ans  = str(sum(map(int, list(ans))))
        print(ans)
        return int(ans)