class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones)==0:
        #     return []
        while(len(stones)>1):
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            if(s1==s2):
                continue
            else:
                stones.append(abs(s1 - s2))
        # print(stones)
        # print(stones[-1])
        if(len(stones)==0):
            return 0
        return stones[-1]