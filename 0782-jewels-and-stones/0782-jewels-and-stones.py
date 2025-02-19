class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)

        ans=0
        
        for i in stones:
            if(i in jewels):
                ans+=1

        print(ans)
        return ans