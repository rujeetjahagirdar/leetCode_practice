class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans=0
        c = Counter(nums) #{3: 3, 1: 1, 4:1}, k=6
        
        for i in list(c.keys()):
            if(k-i in c):
                if((k-i)==i):
                    ans+=c[i]//2
                    # c[i]=0
                    del c[i]
                else:
                    ans+=min(c[i], c[k-i])
                    # c[i]=0
                    # c[k-i]=0
                    del c[i]
                    del c[k-i]
        print(ans)
        return ans
        