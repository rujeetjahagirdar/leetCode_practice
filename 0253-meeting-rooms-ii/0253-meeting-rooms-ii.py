class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        occupiedRooms=0
        # emptyRooms=0
        ans=0
        min_heap = []
        intervals.sort(key= lambda x: x[0])

        #check start if current with min_heap top,
            #while its less than current start, pop from min_heap
        #guess, ans will be len of min_heap
        print(intervals)
        for start, end in intervals:
            if(min_heap and start>=min_heap[0]):
                while(min_heap and min_heap[0]<=start):
                    heapq.heappop(min_heap)
                    occupiedRooms-=1
                heapq.heappush(min_heap, end)
                occupiedRooms+=1
            else:
                occupiedRooms+=1
                heapq.heappush(min_heap, end)
            ans=max(ans, occupiedRooms)
        
            print(min_heap)
            print(ans)
            print(occupiedRooms)
        return ans