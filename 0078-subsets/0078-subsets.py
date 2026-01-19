class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]

        def backtrack(idx, path):
            ans.append(path[:])

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        # for i in range(len(nums)):
        backtrack(0, [])
        
        print(ans)
        return ans