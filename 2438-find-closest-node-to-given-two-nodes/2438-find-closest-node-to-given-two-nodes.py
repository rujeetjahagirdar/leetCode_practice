class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)

        for node, edge in enumerate(edges):
            graph[node].append(edge)
        
        # print(graph)

        node1_reachable = defaultdict(list)
        node2_reachable = defaultdict(list)

        def bfs(node, node_reachable):
            q = deque()
            d=0
            q.append((node, d))
            visited = set()
            
            while(q):
                node, d = q.popleft()
                visited.add(node)
                node_reachable[node].append(d)

                for next_node in graph[node]:
                    if(next_node!=-1 and next_node not in visited):
                        q.append((next_node, d+1))
        
        bfs(node1, node1_reachable)
        # print(node1_reachable)
        bfs(node2, node2_reachable)
        # print(node2_reachable)

        #for every common node, check its distance from node1, node2

        common_nodes = defaultdict(int)

        for common_node in node1_reachable:
            if(common_node in node2_reachable):
                common_nodes[common_node] = max(node1_reachable[common_node], node2_reachable[common_node])
        
        # print(common_nodes)

        if(common_nodes):
            common_nodes = sorted(common_nodes, key=lambda x: (common_nodes[x], x), reverse=False)

            print(common_nodes)
            return(common_nodes[0])
        return -1
        # return(list(common_nodes.keys())[0])