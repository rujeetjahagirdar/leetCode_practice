class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def numberOfOnes(i):
            ans=0
            while(i):
                i = i&(i-1)
                ans+=1
            return ans
        
        a = []
        for i in range(n+1):
            a.append(numberOfOnes(i))
        
        return a