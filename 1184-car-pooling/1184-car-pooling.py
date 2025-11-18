class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        #use min heap to track passengers
        #at each stop, check if any passengers are unloaded at this stop or previous stops and remove them
        #then add current passengers, if excedees capacity, return False

        trips = sorted(trips, key=lambda x: x[1])
        min_heap = [] #(end, number of passangers)
        currentPassangers=0

        for n, s, e in trips:
            while(min_heap and min_heap[0][0]<=s):
                currentPassangers-=heapq.heappop(min_heap)[1]
            
            currentPassangers+=n
            heapq.heappush(min_heap, (e, n))
            if(currentPassangers>capacity):
                return False


        return True