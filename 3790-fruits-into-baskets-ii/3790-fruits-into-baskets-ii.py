class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = len(fruits)

        for f in range(len(fruits)):
            for b in range(len(baskets)):
                if(fruits[f]<=baskets[b]):
                    baskets[b]=0
                    ans-=1
                    break
            # print(ans)
        return(ans)
