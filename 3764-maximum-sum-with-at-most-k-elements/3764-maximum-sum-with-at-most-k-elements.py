class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        largest = []

        for i in range(len(grid)):
            largest.extend(sorted(grid[i], reverse=True)[:limits[i]])
        
        print(largest)
        return(sum(sorted(largest, reverse=True)[:k]))