class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

        # projects = [[capital[i], profits[i]] for i in range(len(profits))]

        # print(projects)

        min_heap = []
        max_heap = []
        ans=0

        for i in range(len(profits)):
            heapq.heappush(min_heap, (capital[i], profits[i]))
        
        for _ in range(k):
            while(min_heap and min_heap[0][0]<=w):
                cap, prof = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-prof, cap))

            if not max_heap:
                break
            
            w += -heapq.heappop(max_heap)[0]
        print(w)
        return w