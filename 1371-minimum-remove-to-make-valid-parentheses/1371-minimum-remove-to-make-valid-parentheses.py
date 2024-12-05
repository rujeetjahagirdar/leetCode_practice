class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)
        stack = []

        for i in range(len(s)):
            if(s[i]=='('):
                stack.append(i)
            elif(s[i]==')'):
                if(len(stack)!=0):
                    if(s[stack[-1]]=='('):
                        stack.pop()
                    else:
                        ans[i]=''
                else:
                    ans[i]=''
        
        while(len(stack)!=0):
            i = stack.pop()
            ans[i]=''
        
        print(ans)
        return ''.join(ans)