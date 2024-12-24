class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_heap = []
        # print(c)
        for i in c:
            if(i%2==0):
                heapq.heappush(max_heap, (-c[i], i))
        # print(max_heap)
        if(max_heap):
            return max_heap[0][1]
        return -1