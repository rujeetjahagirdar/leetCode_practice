class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
#         m, n = len(grid), len(grid[0])
#         totalSum = sum(sum(row) for row in grid)

#         def check(section_sum, other_sum, r1, r2, c1, c2):
#             """Checks if a cell can be removed from section (r1,c1) to (r2,c2) to match other_sum."""
#             diff = section_sum - other_sum
#             if diff == 0: return True
#             if diff < 0: return False # Can't remove a positive int to increase sum
            
#             height = r2 - r1 + 1
#             width = c2 - c1 + 1
            
#             # Connectivity logic
#             if height > 1 and width > 1:
#                 # Any cell in this rectangle can be removed
#                 for r in range(r1, r2 + 1):
#                     for c in range(c1, c2 + 1):
#                         if grid[r][c] == diff: return True
#             elif height == 1:
#                 # Must be ends of the horizontal line
#                 if grid[r1][c1] == diff or grid[r1][c2] == diff: return True
#             elif width == 1:
#                 # Must be ends of the vertical line
#                 if grid[r1][c1] == diff or grid[r2][c1] == diff: return True
#             return False

#         # Horizontal Cuts
#         topSum = 0
#         for i in range(m - 1):
#             topSum += sum(grid[i])
#             botSum = totalSum - topSum
#             if check(topSum, botSum, 0, i, 0, n - 1) or \
#                check(botSum, topSum, i + 1, m - 1, 0, n - 1):
#                 return True

#         # Vertical Cuts
#         leftSum = 0
#         colSums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
#         for j in range(n - 1):
#             leftSum += colSums[j]
#             rightSum = totalSum - leftSum
#             if check(leftSum, rightSum, 0, m - 1, 0, j) or \
#                check(rightSum, leftSum, 0, m - 1, j + 1, n - 1):
#                 return True

#         return False

########################3

        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        # Precompute row and column sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]

        # --- HORIZONTAL CUTS ---
        top_sum = 0
        top_counts = Counter()
        # For the bottom section, start with all values in the grid
        bot_counts = Counter()
        for r in range(m):
            bot_counts.update(grid[r])

        for i in range(m - 1): # Cut after row i
            top_sum += row_sums[i]
            top_counts.update(grid[i])
            bot_counts.subtract(grid[i])
            
            bot_sum = total_sum - top_sum
            
            # Check Top Section (Rows 0 to i)
            diff = top_sum - bot_sum
            if diff == 0: return True
            if diff > 0:
                if (i + 1) > 1 and n > 1:
                    if top_counts[diff] > 0: return True
                elif (i + 1) == 1: # Single Row
                    if grid[0][0] == diff or grid[0][n-1] == diff: return True
                elif n == 1: # Single Column
                    if grid[0][0] == diff or grid[i][0] == diff: return True

            # Check Bottom Section (Rows i+1 to m-1)
            diff = bot_sum - top_sum
            if diff > 0:
                h_bot = m - 1 - i
                if h_bot > 1 and n > 1:
                    if bot_counts[diff] > 0: return True
                elif h_bot == 1: # Single Row
                    if grid[m-1][0] == diff or grid[m-1][n-1] == diff: return True
                elif n == 1: # Single Column
                    if grid[i+1][0] == diff or grid[m-1][0] == diff: return True

        # --- VERTICAL CUTS ---
        left_sum = 0
        left_counts = Counter()
        right_counts = Counter()
        for r in range(m):
            right_counts.update(grid[r])

        for j in range(n - 1): # Cut after col j
            left_sum += col_sums[j]
            # Update counters column by column
            col_vals = [grid[r][j] for r in range(m)]
            left_counts.update(col_vals)
            right_counts.subtract(col_vals)
            
            right_sum = total_sum - left_sum
            
            # Check Left Section (Cols 0 to j)
            diff = left_sum - right_sum
            if diff == 0: return True
            if diff > 0:
                w_left = j + 1
                if m > 1 and w_left > 1:
                    if left_counts[diff] > 0: return True
                elif m == 1: # Single Row
                    if grid[0][0] == diff or grid[0][j] == diff: return True
                elif w_left == 1: # Single Column
                    if grid[0][0] == diff or grid[m-1][0] == diff: return True

            # Check Right Section (Cols j+1 to n-1)
            diff = right_sum - left_sum
            if diff > 0:
                w_right = n - 1 - j
                if m > 1 and w_right > 1:
                    if right_counts[diff] > 0: return True
                elif m == 1: # Single Row
                    if grid[0][j+1] == diff or grid[0][n-1] == diff: return True
                elif w_right == 1: # Single Column
                    if grid[0][n-1] == diff or grid[m-1][n-1] == diff: return True

        return False