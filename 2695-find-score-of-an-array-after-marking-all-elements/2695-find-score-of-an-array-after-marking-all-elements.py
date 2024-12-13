class Solution:
    def findScore(self, nums: List[int]) -> int:
        #while len(marked) not equal nums
            #extract minimum element    
            #mark is and its neighbours if not already marked
            #add this min element to ans

            min_heap = []  #(num, index)

            for i in range(len(nums)):
                heapq.heappush(min_heap, (nums[i], i))
            print(min_heap)

            marked = set()
            ans=0

            while(len(marked)<len(nums)):
                n, i = heapq.heappop(min_heap)
                if(i not in marked):
                    print("min= ", n)
                    ans+=n
                    marked.add(i)
                    if((i-1)>=0 and (i-1) not in marked):
                        marked.add(i-1)
                    if((i+1)<len(nums) and (i+1) not in marked):
                        marked.add(i+1)
            print(marked)
            print(ans)
            return ans