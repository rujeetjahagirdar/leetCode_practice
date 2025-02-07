class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinctColors = defaultdict(int)
        balls = defaultdict(int)
        # balls = [-1]*(limit+1)
        ans=[]
        for b,c in queries:
            if(b not in balls):
                balls[b]=c
                distinctColors[c]+=1
            else:
                distinctColors[balls[b]]-=1
                if(distinctColors[balls[b]]<=0):
                    del distinctColors[balls[b]]
                balls[b]=c
                distinctColors[c]+=1
            ans.append(len(distinctColors))
        print(ans)
        return ans