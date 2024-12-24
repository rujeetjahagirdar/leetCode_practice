class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans=[]
        c = Counter(words)
        max_heap = []
        for i in c:
            heapq.heappush(max_heap,(-c[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        print(ans)
        return ans