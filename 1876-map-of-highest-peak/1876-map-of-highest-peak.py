class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        directions = [(0,1),(1,0), (0,-1), (-1,0)]
        visited = set()

        q = deque()

        def bfs():
            while q:
                i, j = q.popleft()

                for direction in directions:
                    newi, newj = i+direction[0], j+direction[1]
                    if(0<=newi<len(isWater) and 0<=newj<len(isWater[0]) and (newi, newj) not in visited):
                        isWater[newi][newj]=1+isWater[i][j]
                        q.append((newi, newj))
                        visited.add((newi, newj))
            print(isWater)
        

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if(isWater[i][j]==1):
                    q.append((i,j))
                    visited.add((i,j))
                    isWater[i][j]=0
                else:
                    isWater[i][j]=-1
        print(q)
        bfs()
        return(isWater)