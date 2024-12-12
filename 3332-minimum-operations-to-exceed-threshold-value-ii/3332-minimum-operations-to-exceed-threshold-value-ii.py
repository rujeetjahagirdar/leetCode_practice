class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0

        heapq.heapify(nums)

        while(nums[0]<k and len(nums)>=2):
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)

            new_n = min(n1, n2) * 2 + max(n1, n2)

            heapq.heappush(nums, new_n)

            ans+=1
        
        print(ans)
        return ans