class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDegrees = [0] * n
        ans=-1
        for i in edges:
            inDegrees[i[1]] +=1
        print(inDegrees)

        for i in range(len(inDegrees)):
            if(inDegrees[i]==0):
                if(ans==-1):
                    ans=i
                else:
                    return -1
        return ans