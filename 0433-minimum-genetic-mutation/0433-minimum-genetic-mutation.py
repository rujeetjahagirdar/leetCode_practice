class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        visited = set()

        def bfs(startGene):
            q = deque([(startGene, 0)])
            visited.add(startGene)
            while q:
                curr_gene, curr_level = q.popleft()

                if(curr_gene==endGene):
                    return curr_level

                for i in range(len(curr_gene)):
                    for c in 'ACGT':
                        mutation = curr_gene[:i] + c + curr_gene[i+1:]
                        if(mutation in bank and mutation not in visited):
                            q.append((mutation, curr_level+1))
                            visited.add(mutation)
            return -1

        return(bfs(startGene))
