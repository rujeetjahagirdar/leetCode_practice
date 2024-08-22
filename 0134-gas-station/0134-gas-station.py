class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        res = total =0
        if(sum(cost)>sum(gas)):
            return -1
        for i in range(len(gas)):
            total +=(gas[i] - cost[i])
            if total <0:
                total = 0
                res = i+1
        return res