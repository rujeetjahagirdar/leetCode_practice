class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if(self.max_heap and self.min_heap):
            if(-self.max_heap[0]>self.min_heap[0]):
                t = heapq.heappop(self.max_heap)
                t= -t
                heapq.heappush(self.min_heap, t)
        
        if(len(self.max_heap)>len(self.min_heap)+1):
            t = heapq.heappop(self.max_heap)
            t= -t
            heapq.heappush(self.min_heap, t)
        
        if(len(self.min_heap)>len(self.max_heap)+1):
            t = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -t)

    def findMedian(self) -> float:
        if(len(self.max_heap)>len(self.min_heap)):
            return -self.max_heap[0]
        if(len(self.min_heap)>len(self.max_heap)):
            return self.min_heap[0]
        else:
            mdn = (-self.max_heap[0] + self.min_heap[0])/2
            return mdn

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()