class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        aStart = sum([days[i] for i in range(int(arriveAlice[:2])-1)]) + int(arriveAlice[-2:])
        aEnd = sum([days[i] for i in range(int(leaveAlice[:2])-1)]) + int(leaveAlice[-2:])
        bStart = sum([days[i] for i in range(int(arriveBob[:2])-1)]) + int(arriveBob[-2:])
        bEnd = sum([days[i] for i in range(int(leaveBob[:2])-1)]) + int(leaveBob[-2:])

        print(aStart)
        print(aEnd)
        print(bStart)
        print(bEnd)

        if(aEnd < bStart or bEnd < aStart):
            ans = 0
        else:
            ans = min(bEnd, aEnd) - max(aStart, bStart) +1
        
        return(ans)