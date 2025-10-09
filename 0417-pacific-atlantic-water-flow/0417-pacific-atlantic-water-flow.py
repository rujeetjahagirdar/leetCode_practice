class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(q, visited):
            while q:
                i, j = q.popleft()
                for direction in directions:
                    newi, newj = i+direction[0], j+direction[1]
                    # print(i, j)
                    # print(newi, newj)

                    if(0<=newi<len(heights) and 0<=newj<len(heights[0]) and (newi, newj) not in visited and heights[newi][newj]>=heights[i][j]):
                        visited.add((newi, newj))
                        q.append((newi, newj))
        

        pacific_queue = deque()
        pacific_visited = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(i==0 or j==0):
                    pacific_queue.append((i, j))
                    pacific_visited.add((i, j))
        
        bfs(pacific_queue, pacific_visited)
        # print(pacific_visited)
        
        
        atlantic_queue = deque()
        atlantic_visited = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(i==len(heights)-1 or j==len(heights[0])-1):
                    atlantic_queue.append((i, j))
                    atlantic_visited.add((i, j))
        
        bfs(atlantic_queue, atlantic_visited)
        # print(atlantic_visited)

        ans=[]
        for i in pacific_visited:
            if(i in atlantic_visited):
                ans.append([i[0], i[1]])

        return(ans)