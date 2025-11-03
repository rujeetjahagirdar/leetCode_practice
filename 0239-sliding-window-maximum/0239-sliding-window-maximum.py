class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = [max(nums[:k])]

        # for i in range(1, len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        
        # return(ans)


#####################3

        ans=[]
        max_heap = []

        if(len(nums)==1):
            return [nums[0]]

        for i in range(k-1):
            heapq.heappush(max_heap, (-nums[i], i))
        
        # print(max_heap)
        
        for i in range(k-1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            while(max_heap[0][1]<=(i-k)):
                heapq.heappop(max_heap)
            
            # print(max_heap)
            
            ans.append(-max_heap[0][0])
        
        
        return(ans)