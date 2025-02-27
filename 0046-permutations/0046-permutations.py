class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if start == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(start + 1, path)
                    path.pop()
        result = []
        backtrack(0, [])
        return result
#Runtime Complexity: O(n*n!)
#Space Complexity: O(n*n)