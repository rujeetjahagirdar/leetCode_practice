class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []

        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i], i))
        
        for _ in range(k):
            min_val, min_val_index = heapq.heappop(min_heap)
            new_val = min_val * multiplier
            heapq.heappush(min_heap, (new_val, min_val_index))
            nums[min_val_index] = new_val
        print(nums)
        return nums