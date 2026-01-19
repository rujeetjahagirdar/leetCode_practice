class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        used = set()

        def backtrack(start, path):
            if(len(path)==len(nums)):
                ans.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if(i in used):
                    continue
                path.append(nums[i])
                used.add(i)
                # print(path)
                backtrack(i, path)
                path.pop()
                used.remove(i)
        

        backtrack(0, [])

        print(ans)
        return ans