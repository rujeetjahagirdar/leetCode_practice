class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        ans=0

        for i in range(len(s)):
            #if (, append to stack
            #else, 
                #if stack: pop stack pop
                    #valid length = current - stack top
                    #if stack becomes empty append current index
                #else:
                    #append current index
            
            if(s[i]=='('):
                stack.append(i)
            else:
                stack.pop()

                if(not stack):
                    stack.append(i)
                else:
                    ans = max(ans, (i- stack[-1]))
            
        return ans