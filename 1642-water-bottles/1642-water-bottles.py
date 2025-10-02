class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=0
        empty=0

        while(numBottles>0):
            ans+=numBottles
            empty+=numBottles
            numBottles=0

            if(empty>=numExchange):
                numBottles+=1
                empty-=numExchange
            print(ans)
        return ans