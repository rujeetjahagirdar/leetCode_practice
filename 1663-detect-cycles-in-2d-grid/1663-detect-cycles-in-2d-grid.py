class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        

        def dfs(i, j, strt, prnt):
            # if((i, j) in visited):
            #     if((i, j)==strt):
            #         return True
            #     else:
            #         return

            if((i, j) in visited):
                return True
            
            visited.add((i, j))

            for direction in directions:
                newi, newj = i+direction[0], j+direction[1]
                if(0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]==grid[i][j] and (newi, newj)!=prnt):
                    if dfs(newi, newj, strt, (i, j)):
                        return True
            
            return False
        

        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if((row, col) not in visited):
                    # visited.add((row, col))
                    start = (row, col)
                    parent = (row, col)
                    found = dfs(row, col, start, parent)
                    if(found):
                        return True
        
        return False
        