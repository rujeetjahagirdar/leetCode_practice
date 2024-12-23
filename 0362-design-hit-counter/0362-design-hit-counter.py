class HitCounter:

    def __init__(self):
        self.min_heap = []

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.min_heap, timestamp)

    def getHits(self, timestamp: int) -> int:
            start_time = timestamp-300 #seconds
            while(self.min_heap and self.min_heap[0]<=start_time):
                heapq.heappop(self.min_heap)
                
            return(len(self.min_heap))



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)