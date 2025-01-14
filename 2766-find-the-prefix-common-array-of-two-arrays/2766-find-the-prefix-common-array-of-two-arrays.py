class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freqA = set()
        freqB = set()
        ans=[0]*(len(A)+1)

        for i in range(len(A)):
            t=0
            if(A[i]==B[i]):
                t+=1
            if(B[i] in freqA):
                t+=1
            if(A[i] in freqB):
                t+=1
            ans[i+1] = ans[i]+t
            freqB.add(B[i])
            freqA.add(A[i])
        print(freqA)
        print(freqB)
        print(ans)
        return ans[1:]