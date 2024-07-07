class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(s):
            s=str(s)
            count=0
            for i in s:
                if(i=='1'):
                    count=count+1
            return count
        ans=[]
        for i in range(n+1):
            ans.append(countOnes(bin(i)))
        print(ans)
        return ans