class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        
        for num in nums:
            # Update the new max rob amount considering the current house
            current = max(prev1 + num, prev2)
            # Move the window: prev2 becomes the new prev1, current becomes prev2
            prev1, prev2 = prev2, current
        
        return prev2
