class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        #{1: 3, 2:2, 3:1}, k=2

        min_heap = []

        for i in c:
            if(len(min_heap)<k):
                heapq.heappush(min_heap, (c[i], i))
            else:
                if(c[i]<min_heap[0][0]):
                    continue
                else:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (c[i], i))
            print(min_heap)
        ans=[]

        while min_heap:
            ans.append(heapq.heappop(min_heap)[1])
        return ans