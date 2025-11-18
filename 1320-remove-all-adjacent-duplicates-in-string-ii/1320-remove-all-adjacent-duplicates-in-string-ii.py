class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        
        
        stack = [] #(lastChar, freq of lastChar)

        if(not s):
            return ''
        
        # stack.append((s[0], 1))

        for i in range(len(s)):
            if(stack):
                if(s[i]==stack[-1][0]):
                    stack[-1] = (stack[-1][0], stack[-1][1]+1)
                else:
                    stack.append((s[i], 1))
            else:
                stack.append((s[i], 1))
            
            if(stack[-1][1]>=k):
                stack.pop()
        
        print(stack)

        ans=''

        for c, f in stack:
            ans+=c*f
        
        return(ans)