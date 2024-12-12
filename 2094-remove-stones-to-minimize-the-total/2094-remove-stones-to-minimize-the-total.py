class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []

        for i in piles:
            heapq.heappush(max_heap, -i)
        
        for _ in range(k):
            max_stones = -1 * heapq.heappop(max_heap)
            remaining_stones = max_stones - math.floor(max_stones/2)
            heapq.heappush(max_heap, -1 * remaining_stones)
        
        return(-1 * sum(max_heap))