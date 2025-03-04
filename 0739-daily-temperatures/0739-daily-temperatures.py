class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)

        stack = [0]

        for j in range(1, len(temperatures)):
            while(stack and temperatures[j]>temperatures[stack[-1]]):
                i = stack.pop()
                ans[i] = (j-i)
            stack.append(j)
        print(ans)
        return ans