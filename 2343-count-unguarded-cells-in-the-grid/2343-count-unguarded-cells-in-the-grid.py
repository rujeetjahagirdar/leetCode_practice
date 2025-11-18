class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        #from each guard, traverse in all four directions
        ans=0
        unguarded_cells = set()
        guarded_cells = set()

        guard_cells = set()
        for i, j in guards:
            guard_cells.add((i, j))

        walls_set = set()
        for i, j in walls:
            walls_set.add((i, j))
        
        for guardi, guardj in guards:

            #go up
            for i in range(guardi-1, -1, -1):
                if((i, guardj) in guard_cells or (i, guardj) in walls_set):
                    break
                guarded_cells.add((i, guardj))
            
            #go right
            for j in range(guardj+1, n):
                if((guardi, j) in guard_cells or (guardi, j) in walls_set):
                    break
                guarded_cells.add((guardi, j))
            
            #go down
            for i in range(guardi+1, m):
                if((i, guardj) in guard_cells or (i, guardj) in walls_set):
                    break
                guarded_cells.add((i, guardj))
            
            #go left
            for j in range(guardj-1, -1, -1):
                if((guardi, j) in guard_cells or (guardi, j) in walls_set):
                    break
                guarded_cells.add((guardi, j))
            
        for i in range(m):
            for j in range(n):
                if((i, j) not in guarded_cells and (i, j) not in guard_cells and (i, j) not in walls_set):
                    unguarded_cells.add((i, j))
                    ans+=1
        
        return(ans)