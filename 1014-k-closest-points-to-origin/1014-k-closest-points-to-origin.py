class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #for finding smallest k elements we use max heap
        #and to find largest k elements we use min heap

        max_heap = []

        for x, y in points:
            dist = math.sqrt(x*x + y*y)

            if(len(max_heap)<k):
                heapq.heappush(max_heap, (-dist, (x, y)))
            else:
                if(dist>= -max_heap[0][0]):
                    continue
                else:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist, (x, y)))
        ans = []

        while max_heap:
            ans.append(heapq.heappop(max_heap)[1])
        
        return ans