class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        ans=[]

        for x, y in points:
            d = math.sqrt(x**2 + y**2)

            if(len(max_heap)<k):
                heapq.heappush(max_heap, (-d, x, y))
            else:
                if(d<-max_heap[0][0]):
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-d, x, y))
        
        for d, x, y in max_heap:
            ans.append([x, y])
        
        return ans