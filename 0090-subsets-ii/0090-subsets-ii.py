class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        nums.sort()

        def backtrack(start, path):
            ans.append(path[:])

            for i in range(start, len(nums)):
                if(i>start and nums[i]==nums[i-1]): #[1,2,2], using i>start allows first '2' to be included but prevents second '2' from inclusion (basically prevents duplicates)
                    continue
                path.append(nums[i])
                print(path)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])

        print(ans)
        return ans