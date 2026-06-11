class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        #build adjcency list
        #do DFS and max depth
        #and to get odd weight, there should be odd number of odd weights in the path

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # print(adj)
        
        max_depth = 0
        visited = set()
        
        def dfs(node, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            visited.add(node)

            for neighbour in adj[node]:
                if(neighbour not in visited):
                    dfs(neighbour, depth+1)
        
        dfs(1, 0)
        # print(f"max_depth= {max_depth}")


        ans = pow(2, max_depth-1)

        return ans % (10**9 + 7)
