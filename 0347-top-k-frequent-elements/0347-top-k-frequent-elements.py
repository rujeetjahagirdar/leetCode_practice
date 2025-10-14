class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #TC: O(n logk)
        #SC: O(n)

        #freq counter
        #min_heap

        # nums = [1,1,1,2,2,3], k = 2

        c = Counter(nums)

        #{1: 3, 2:2, 3:1}, k=2
        #[(3, 1)]
        #[(3, 1), (2, 2)]
        #[(2, 2), (3, 1)]
        #[(2, 2), (3, 1)]

        #Example 2
        #{1: 3, 2:2, 3:3}, k=2
        #[(3, 1)]
        #[(3, 1), (2, 2)]
        #[(2, 2), (3, 1)]
        #[(3, 1)]
        #[(3, 1), (3, 3)]

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
        
        ans=[]

        for i in min_heap:
            ans.append(i[1])
        
        return ans