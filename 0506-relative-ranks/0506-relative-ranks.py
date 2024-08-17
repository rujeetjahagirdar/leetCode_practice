class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if(len(score)==1):
            return ["Gold Medal"]
        elif(len(score)==2):
            for i in score:
                if i==max(score):
                    return ["Gold Medal", "Silver Medal"]
                else:
                    return ["Silver Medal", "Gold Medal"]
        else:
            sortedScore = sorted(score, reverse=True)
            # print(sortedScore)
            fstRnk,scndRnk, thrdRnk = sortedScore[0], sortedScore[1], sortedScore[2]
            ans = []
            for i in score:
                if(i==fstRnk):
                    ans.append("Gold Medal")
                elif(i==scndRnk):
                    ans.append("Silver Medal")
                elif(i==thrdRnk):
                    ans.append("Bronze Medal")
                else:
                    ans.append(str(sortedScore.index(i)+1))
        return(ans)