class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        def dfs(i, j):
            # print(i, j)
            if(visited[i][j]==True):
                return
            
            visited[i][j]=True

            if(i==destination[0] and j==destination[1]):
                return
            
            for direction in directions:
                newi, newj = i, j

                while(0<=newi+direction[0]<len(maze) and 0<=newj+direction[1]<len(maze[0]) and maze[newi+direction[0]][newj+direction[1]]==0):
                    newi = newi + direction[0]      #keep moving in same direction till hit the wall
                    newj = newj + direction[1]
                
                #when hit the wall, dfs from there
                # print(newi, newj)
                dfs(newi, newj)

        

        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        # print(visited)
        directions = [(-1, 0), (0,1), (1, 0), (0, -1)]
        

        dfs(start[0], start[1])

        return visited[destination[0]][destination[1]]