class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtrack(start, remaining, path):
            if remaining==0:
                ans.append(path[:])
            
            if(remaining<0):
                return 
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # print(path)
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        

        backtrack(0, target, [])

        print(ans)
        return ans