class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # nums.sort()
        ans = 0
        c= Counter(nums)
        for i in c:
            if i+1 in c:
                counts = c[i] + c[i+1]
                if counts>ans:
                    ans = counts
                
        return ans