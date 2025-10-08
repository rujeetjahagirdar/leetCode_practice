class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        #(lastChar, freq of lastChar)
        stack = []

        

        for i in range(len(s)):

            if(stack and s[i]==stack[-1][0]):
                char, freq = stack.pop()
                stack.append((char, freq+1))
            else:
                stack.append((s[i], 1))
            
            if(stack[-1][1]==k):
                stack.pop()
            # print(stack)
        
        ans=''

        for i in stack:
            ans+=i[0]*i[1]
        # print(ans)
        return ans