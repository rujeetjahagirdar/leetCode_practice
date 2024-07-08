class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        # for i in range(len(temperatures)):
        #     days=1
        #     # print(temperatures[i])
        #     for j in range(i+1,len(temperatures)):
        #         if(temperatures[j]>temperatures[i]):
        #             ans[i]=days
        #             break
        #         else:
        #             days = days + 1
        # return(ans)
        for i in range(len(temperatures)):
            while(stack and temperatures[i]>temperatures[stack[-1]]):
                previous_index = stack.pop()
                ans[previous_index] = i - previous_index
            stack.append(i)
            # print(stack)

        return(ans)