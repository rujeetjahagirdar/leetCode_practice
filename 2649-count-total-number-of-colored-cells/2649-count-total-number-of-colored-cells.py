class Solution:
    def coloredCells(self, n: int) -> int:
        # ans=1

        # for i in range(1, n):
        #     ans+=4*i
        #     # print(ans)
        # return ans
        ####################

        return (((n*(n-1))//2)*4)+1