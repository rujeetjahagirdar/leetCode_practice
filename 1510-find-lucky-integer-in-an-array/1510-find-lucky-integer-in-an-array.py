class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=-1
        c= Counter(arr)

        for i in c:
            if(i==c[i]):
                ans=max(ans, i)
        
        return ans