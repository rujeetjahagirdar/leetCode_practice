class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans=0
        if(len(cost)<=2):
            return sum(cost)
        cost = sorted(cost, reverse=True)

        for i in range(0, len(cost), 3):
            if(i+1>=len(cost) or i+2>=len(cost)):
                print(cost[i:])
                ans+=sum(cost[i:])
                break
            print(cost[i], cost[i+1], cost[i+2])
            ans+=(cost[i]+cost[i+1])
        
        return(ans)