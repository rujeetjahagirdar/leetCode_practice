from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, one at the start and one at the end of the array
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width of the current container
            width = right - left
            # Calculate the height of the current container (the minimum of the two lines)
            container_height = min(height[left], height[right])
            # Calculate the area of the current container
            area = width * container_height
            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

            # Move the pointer of the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Runtime Complexity: O(n)
# Space Complexity: O(1)