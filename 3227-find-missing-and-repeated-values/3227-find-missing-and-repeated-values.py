class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans=[]
        n=len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                if(grid[i][j] in seen):
                    ans.append(grid[i][j])
                seen.add(grid[i][j])
                total+=grid[i][j]
        
        totalN = n*n
        actualTotal = (totalN*(totalN+1))//2
        diff = actualTotal - total
        ans.append(ans[0]+diff)

        print(ans)
        return ans