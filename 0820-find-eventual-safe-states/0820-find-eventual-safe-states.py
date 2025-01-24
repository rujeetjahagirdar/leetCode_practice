class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        terminal=set()
        path = []


        def dfs(i):
            if(i in visited):
                if(i in terminal):
                    return True
                else:
                    return False

            visited.add(i)
            path.append(i)
            # print(path)
            
            for n in graph[i]:
                if(n in path or dfs(n)==False):
                    return False
            
            terminal.add(i)
            path.remove(i)
            
            return True
            
        

        for i in range(len(graph)):
            dfs(i)
        
        print(terminal)
        return sorted(terminal)