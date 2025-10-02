class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        

        #while fullbottles not zero and empty bottle >=nuExchange:
            #ans+=fulbottles
            #empty+=fullbottles
            #fullbottles = emptybottles//numExchange
            #numExchange+=1
            #
        
        ans=0
        empty=0

        while(numBottles!=0):
            ans+=numBottles
            empty+=numBottles
            numBottles=0
            if(empty>=numExchange):
                numBottles+=1
                empty-=numExchange
                numExchange+=1
        return(ans)