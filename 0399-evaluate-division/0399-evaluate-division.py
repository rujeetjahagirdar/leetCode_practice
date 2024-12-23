class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a = 2b
        #b = 3c
        #a=6c
        mapping = defaultdict(dict)

        for i in range(len(equations)):
            mapping[equations[i][0]][equations[i][1]] = values[i]
            mapping[equations[i][1]][equations[i][0]] = 1/values[i]
        print(mapping)

        #{'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}}


        def dfs(currentDeno, targetDeno, visited, product):
            if currentDeno not in mapping or targetDeno not in mapping:
                return -1
            if currentDeno ==targetDeno:
                return product
            else:
                visited.add(currentDeno)
                for neighbour in mapping[currentDeno]:
                    if neighbour not in visited:
                        result = dfs(neighbour, targetDeno, visited, product * mapping[currentDeno][neighbour])
                        if(result!=-1):
                            return result
                return -1
                
        
        ans=[]
        for i in range(len(queries)):
            visited = set()
            visited.add(queries[i][0])
            ans.append(dfs(queries[i][0], queries[i][1], visited, 1))
        
        print(ans)
        return ans