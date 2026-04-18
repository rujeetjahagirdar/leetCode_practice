class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        #hashmap: sorted number and its last index
        #store reversed number in hashM

        hashM = {}
        ans = float("inf")

        for i in range(len(nums)):
            if(nums[i] in hashM):
                ans = min(ans, i-(hashM[nums[i]]))
            
            revNum = int(str(nums[i])[::-1])
            hashM[revNum] = i
        
        if(ans==float("inf")):
            return -1
        return ans