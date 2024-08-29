class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tNums = []
        for i, v in enumerate(nums):
            tNums.append((v,i))
        tNums = sorted(tNums, key = lambda x:x[0])
        ans = tNums[-k:]
        print(tNums[-k:])
        ans = sorted(ans, key= lambda x: x[1])
        ans2 = [i[0] for i in ans]
        return ans2
        