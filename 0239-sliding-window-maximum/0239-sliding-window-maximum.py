class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = [max(nums[:k])]

        # for i in range(1, len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        
        # return(ans)


######################

        #maintain window as max heap of (value,index)
        #add new element
            #remove all the elemts from window with index less than current (index-k)

        # ans=[]
        # max_heap = []

        # if(len(nums)==1):
        #     return [nums[0]]

        # for i in range(k):
        #     heapq.heappush(max_heap, (-nums[i], i))
        
        # ans.append(-max_heap[0][0])
        
        # # print(max_heap)
        
        # for i in range(k, len(nums)):
        #     heapq.heappush(max_heap, (-nums[i], i))

        #     print(max_heap)

        #     #if new element is greater than current max (last window's max/heap top), then no pop
        #     #if new element is less than or equal than current max (last window's max/heap top) and it is outside current window then pop if not outside current window, no pop

        #     while(max_heap[0][1]<=(i-k)):
        #         heapq.heappop(max_heap)
            
        #     print("after= ",max_heap)
            
        #     ans.append(-max_heap[0][0])
        
        
        # return(ans)

######################

# Approach 2:

# maintain double ended queue in descreaing order
# while adding new element, 
    # remove all outside window elements from left of queue
    # remove all elements less than equal to current element from right of queue
#append left most element of queue to ans

        dq = deque()
        ans= []

        for i in range(len(nums)):
            while(dq and dq[0]<=(i-k)):
                dq.popleft()
            
            while(dq and nums[dq[-1]]<=nums[i]):
                dq.pop() #popright
            
            dq.append(i)

            if(i>=k-1):
                ans.append(nums[dq[0]])
        return(ans)