class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in nums:
            if(len(min_heap)>=k):
                if(i>min_heap[0]):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, i)
            else:
                heapq.heappush(min_heap, i)
        
        print(min_heap)
        return min_heap[0]