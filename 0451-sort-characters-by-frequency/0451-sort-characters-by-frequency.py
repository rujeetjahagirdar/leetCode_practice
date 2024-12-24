class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        max_heap = []
        c = Counter(s)

        for i in c:
            heapq.heappush(max_heap, (-c[i], i))
        
        while max_heap:
            f, c = heapq.heappop(max_heap)
            f=-f
            ans+=c*f
        print(ans)
        return ans
