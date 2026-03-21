class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for row in range(k//2):
            for col in range(k):
                grid[x+row][y+col], grid[x+k-1 - row][y+col] = grid[x+k-1 - row][y+col], grid[x+row][y+col]
        
        print(grid)

        return grid