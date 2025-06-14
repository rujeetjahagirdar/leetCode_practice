class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winners = [i+1 for i in range(n)]
        curr=0

        while(len(winners)!=1):
            curr = (curr+k-1)%len(winners)
            # curr = nxt+1
            winners.pop(curr)
        
        return(winners[0])