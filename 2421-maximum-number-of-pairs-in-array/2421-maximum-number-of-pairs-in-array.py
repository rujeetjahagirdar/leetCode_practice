class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pairsCount = 0
        
        for i in c:
            pairsCount+=c[i]//2

        remianingCount = len(nums) - (2*pairsCount)
        print(pairsCount)
        print(remianingCount)
        return [pairsCount ,remianingCount]
