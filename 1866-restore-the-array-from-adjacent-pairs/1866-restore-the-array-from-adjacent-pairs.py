class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        def dfs(node, ans):
            ans.append(node)
            for neighbour in adjacency_graph[node]:
                if(neighbour not in visited):
                    visited.add(neighbour)
                    dfs(neighbour, ans)


        adjacency_graph = defaultdict(list)

        for n1, n2 in adjacentPairs:
            adjacency_graph[n1].append(n2)
            adjacency_graph[n2].append(n1)
        

        # print(adjacency_graph)

        ans=[]
        visited = set()

        start_node = -1
        for i in adjacency_graph:
            if(len(adjacency_graph[i])==1):
                start_node = i
                break
        
        visited.add(start_node)
        dfs(start_node, ans)

        print(ans)
        return ans