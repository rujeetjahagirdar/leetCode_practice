class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq_count = {}
        freq_freq_count = {}

        for i in nums:
            freq_count[i] = freq_count.get(i, 0) + 1
        
        for f in freq_count.values():
            freq_freq_count[f] = freq_freq_count.get(f, 0) + 1
        


        for i in nums:
            if(freq_freq_count[freq_count[i]]==1):
                return i
        
        return -1