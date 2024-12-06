class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        #[1,2,3,4,5]

        bannedSet = set(banned)
        print(bannedSet)
        ans=0
        sumCurrent=0
        for i in range(1, n+1):
            if(i not in bannedSet):
                if(sumCurrent+i<=maxSum):
                    sumCurrent+=i
                    ans+=1
                else:
                    return ans
            else:
                continue
        return ans