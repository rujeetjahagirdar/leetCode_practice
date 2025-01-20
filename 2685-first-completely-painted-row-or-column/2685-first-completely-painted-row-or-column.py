class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Map number -> (row, column) in mat
        position_map = {}
        for r in range(m):
            for c in range(n):
                position_map[mat[r][c]] = (r, c)
        
        # Track the count of painted cells in each row and column
        rows_painted = [0] * m
        cols_painted = [0] * n
        
        # Process the painting sequence
        for i, num in enumerate(arr):
            r, c = position_map[num]
            rows_painted[r] += 1
            cols_painted[c] += 1
            
            # If entire row or column is painted, return the index
            if rows_painted[r] == n or cols_painted[c] == m:
                return i
        
        return -1  # Should never reach here since a full row/col is guaranteed to be painted
