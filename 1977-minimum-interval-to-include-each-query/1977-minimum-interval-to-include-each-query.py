class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_intervals = sorted(intervals, key= lambda x: x[0])
        queries2 = [(queries[i], i) for i in range(len(queries))]

        sorted_queries2 = sorted(queries2, key = lambda x : x[0])

        ans=[-1]*len(queries)
        min_heap = []
        i=0

        print(sorted_intervals)
        print(sorted_queries2)

        for q in sorted_queries2:
            # print(q)
            # t_ans = float("inf")
            # i=0

            #first, add all candidate intervals
            while(i<len(sorted_intervals) and q[0]>=sorted_intervals[i][0]):
                # if(sorted_intervals[i][0]<=q[0]<=sorted_intervals[i][1]):
                #     # print(sorted_intervals[i][0], sorted_intervals[i][1])
                #     t_ans = min(t_ans, sorted_intervals[i][1] - sorted_intervals[i][0] +1)
                l, r = sorted_intervals[i][0], sorted_intervals[i][1]
                size = r - l +1
                heapq.heappush(min_heap, (size, r))
                i+=1
            
            #second, remove invalid intervals from these candidates
            while(min_heap and min_heap[0][1]<q[0]):
                heapq.heappop(min_heap)
            
            #if any intervals remains in min_heap, it will having min size
            if(min_heap):
                ans[q[1]] = min_heap[0][0]

            # ans[q[1]] = t_ans
            # print(ans)
        
        print(ans)
        for i in range(len(ans)):
            if(ans[i]==float("inf")):
                ans[i]=-1
        return ans