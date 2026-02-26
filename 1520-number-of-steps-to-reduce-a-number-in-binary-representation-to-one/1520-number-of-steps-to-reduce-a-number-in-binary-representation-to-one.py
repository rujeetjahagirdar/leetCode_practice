class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        n = int(s, 2)
        # print(n)

        while(n!=1):
            if(n%2==0):
                n//=2
            else:
                n+=1
            ans+=1
        
        # print(ans)
        return ans