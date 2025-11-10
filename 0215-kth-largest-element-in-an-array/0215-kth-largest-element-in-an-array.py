class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #since we need to find the larget, we will use min_heap, so it will store right portion of the sorted array

        min_heap = []

        for n in nums:
            if(len(min_heap)<k):
                heapq.heappush(min_heap, n)
            
            else:
                #if greater than min_heap[0], then push
                #else ignore
                if(n>min_heap[0]):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, n)
        
        return(min_heap[0])