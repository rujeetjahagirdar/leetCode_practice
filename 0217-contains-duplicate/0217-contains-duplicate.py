class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))!=len(nums)
        freq = Counter(nums)
        for i in freq:
            if(freq[i]>1):
                return True
        return False