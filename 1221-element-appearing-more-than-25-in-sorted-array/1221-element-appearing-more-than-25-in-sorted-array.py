class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        requiredFreq = len(arr)//4
        c = Counter(arr)

        for i in c:
            if(c[i]>requiredFreq):
                return i