class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = nums[0].copy()

        for i in nums[0]:
            for j in range(1,len(nums)):
                print(i, nums[j])
                if i not in nums[j]:
                    ans.remove(i)
                    break
            # ans.append(i)
        ans.sort()
        return ans