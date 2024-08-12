class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        chart = {}
        ans=0
        for player, color in pick:
            if(player not in chart):
                chart[player] = [0]*11
                # print(chart)
                chart[player][color] +=1
            else:
                chart[player][color] +=1
        print(chart)
        for k in chart:
            for i in chart[k]:
                if i>=k+1:
                    ans +=1
                    break
        print(ans)
        
        return ans        