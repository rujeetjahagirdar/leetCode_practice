class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0

        sSet = set(s)

        for l in sSet:
            firstIdx = s.index(l)
            lastIdx = s.rindex(l)

            uniqueBetween = set()

            for i in range(firstIdx+1, lastIdx):
                if(s[i] not in uniqueBetween):
                    uniqueBetween.add(s[i])
            ans+=len(uniqueBetween)
            print(ans)
        return ans