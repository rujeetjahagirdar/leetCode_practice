class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #heap, max_heap

        max_heap = []

        for x, y in points:
            distance = math.sqrt(x*x + y*y)

            if(len(max_heap)<k):
                heapq.heappush(max_heap, (- distance, x, y))
            else:
                if(distance< -(max_heap[0][0])):
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (- distance, x, y))
        
        ans=[]

        for d, x, y in max_heap:
            ans.append([x, y])
        
        return(ans)