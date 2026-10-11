class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n1 = bin(x)[2:]
        n2 = bin(y)[2:]

        n1 = n1.rjust(len(n2), '0')
        n2 = n2.rjust(len(n1), '0')

        ans=0

        # print(n1, n2)

        for i in range(len(n1)):
            if(n1[i]!=n2[i]):
                ans+=1
        
        return ans