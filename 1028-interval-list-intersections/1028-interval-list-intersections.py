class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]

        if(not firstList or not secondList):
            return []

        i=j=0

        while(i<len(firstList) and j<len(secondList)):
            if(firstList[i][0]>secondList[j][1]):
                j+=1
                continue
            if(secondList[j][0]>firstList[i][1]):
                i+=1
                continue
            aStart = max(firstList[i][0], secondList[j][0])
            aEnd = min(firstList[i][1], secondList[j][1])
            ans.append([aStart, aEnd])

            if(firstList[i][1]<secondList[j][1]):
                i+=1
            else:
                j+=1
        # #check remaining in first list
        # while(i<len(firstList)-1):
        #     ans.append(firstList[i])
        #     i+=1
        # #check remaining in second list
        # while(j<len(secondList)-1):
        #     ans.append(secondList[j])
        #     j+=1
        
        return(ans)