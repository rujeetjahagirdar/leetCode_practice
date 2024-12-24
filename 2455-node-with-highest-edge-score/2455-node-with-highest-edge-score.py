class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edge_scores = defaultdict(list)

        for i in range(len(edges)):
            edge_scores[edges[i]].append(i)
        
        print(edge_scores)
        ans = -1
        max_score = float("-inf")

        for i in edge_scores:
            if(sum(edge_scores[i])>=max_score):
                if(sum(edge_scores[i])==max_score):
                    ans = min(i, ans)
                else:
                    ans=i
                max_score = sum(edge_scores[i])
        print(ans)
        return ans