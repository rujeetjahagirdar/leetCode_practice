class Solution:
    def halveArray(self, nums: List[int]) -> int:
        #while loop till total sum is less than or equal to initial sum
        #since we want minimum number of operations, we should choose max number from array to reduce

        initial_sum = sum(nums)

        max_heap = []
        for i in nums:
            heapq.heappush(max_heap, -i)
        
        ans=0
        heap_sum = initial_sum
        while(heap_sum>(initial_sum/2)):
            max_num = -1 * heapq.heappop(max_heap)
            max_num = max_num /2
            heap_sum -=max_num
            heapq.heappush(max_heap, -1 * max_num)
            ans+=1
        
        print(ans)
        return ans