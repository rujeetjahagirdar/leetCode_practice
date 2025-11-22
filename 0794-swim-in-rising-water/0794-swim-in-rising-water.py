class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        #Dijkstra algo, basically, BFS but instead of queue use min_heap
        #min_heap will globally minim path to destination, i.e. minimum path of all paths

        min_heap = []
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = float("-inf")

        parents = defaultdict(set) #this is to keep track of from which parent node did we reach current node
        
        heapq.heappush(min_heap, (grid[0][0], 0, 0)) #(height, row, col)
        visited.add((0,0))
        parents[(0,0)] = None


        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            ans = max(ans, grid[r][c])

            if(r==len(grid)-1 and c==len(grid)-1):
                print(ans)
                print(parents)
                break
            
            for direction in directions:
                newr, newc = r+direction[0], c+direction[1]

                if(0<=newr<len(grid) and 0<=newc<len(grid) and (newr, newc) not in visited):
                    parents[(newr, newc)] = (r, c)
                    heapq.heappush(min_heap, (grid[newr][newc], newr, newc))
                    visited.add((newr, newc))
            
        #build path backwards
        path = []

        curr = (len(grid)-1, len(grid)-1)

        while curr!=None:
            i, j = curr[0], curr[1]
            path.append(grid[i][j])
            curr = parents[curr]
        
        path = path[::-1]

        print(path)

        return ans