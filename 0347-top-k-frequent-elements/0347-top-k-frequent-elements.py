class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #counter with min heap

        min_heap = []
        ans=[]

        c = Counter(nums)
        # print(c)

        for n in c:
            if(len(min_heap)<k):
                heapq.heappush(min_heap, (c[n], n))
            else:
                if(c[n]>min_heap[0][0]):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (c[n], n))
        
        # print(min_heap)

        for i in min_heap:
            ans.append(i[1])
        
        return ans