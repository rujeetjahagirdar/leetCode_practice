class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        min_heap = [] #(-1*freq, num)
        c = Counter(nums)
        for i in c:
            heapq.heappush(min_heap, (c[i], -i))
        print(min_heap)
        ans=[]
        while min_heap:
            f, n = heapq.heappop(min_heap)
            ans.extend([-n] * f)

        print(ans)
        return ans