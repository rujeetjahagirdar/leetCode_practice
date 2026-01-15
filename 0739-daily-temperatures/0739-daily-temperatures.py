class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)

        stack = [0]

        #for each element in temperatures, all of its previous elements will be poped and only current element is pushed, so effectively every element is pushed only once and poped only once, so it will be O(n)

        for j in range(1, len(temperatures)):
            while(stack and temperatures[j]>temperatures[stack[-1]]):
                i = stack.pop()
                ans[i] = (j-i)
            stack.append(j)
        print(ans)
        return ans

        