class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i,j = 0, 0
        # mn = nums[0]
        # mx = nums[0]
        max_heap = []
        min_heap = []
        ans=0

        while(j<len(nums)):
            heapq.heappush(max_heap, (-nums[j], j))
            heapq.heappush(min_heap, (nums[j], j))

            if(-max_heap[0][0]-min_heap[0][0]>2):
                while(-max_heap[0][0]-min_heap[0][0]>2 and i<j):
                    i+=1

                    while(min_heap and min_heap[0][1]<i):
                        heapq.heappop(min_heap)
                    while(max_heap and max_heap[0][1]<i):
                        heapq.heappop(max_heap)
            ans += (j-i+1)
            j+=1
        print(ans)
        return ans
