class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x1, y1 in points:
            dist = math.sqrt(x1**2+y1**2)

            if(len(max_heap)<k):
                heapq.heappush(max_heap, (-dist, [x1, y1]))
            else:
                # print(dist)
                if(dist<-max_heap[0][0]):
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist, [x1, y1]))
        
            # print(max_heap)
        ans=[]
        for i in max_heap:
            ans.append(i[1])
        print(ans)
        return ans
