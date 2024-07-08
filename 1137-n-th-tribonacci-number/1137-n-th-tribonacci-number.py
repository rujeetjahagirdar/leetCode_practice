class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            ans=[0,1,1]
            for i in range(3,n+1):
                ans.append(ans[-1]+ans[-2]+ans[-3])
        # print(ans)
        return ans[-1]