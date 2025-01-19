from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        write_index = 2
        for read_index in range(2, len(nums)):
            if nums[read_index]!= nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index

# Runtime Complexity: O(n)
# Space Complexity: O(1)