class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for i in gifts:
            heapq.heappush(max_heap, -i)
        print(max_heap)

        for _ in range(k):
            max_gifts = -heapq.heappop(max_heap)
            remaining_gifts  = math.floor(math.sqrt(max_gifts))
            heapq.heappush(max_heap, -remaining_gifts)
        
        print(max_heap)
        return(-1*sum(max_heap))