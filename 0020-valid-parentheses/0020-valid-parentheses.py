class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if(i in ('(', '{', '[')):
                stack.append(i)
            else:
                if(len(stack)>0):
                    if(i==')' and stack[-1]=='('):
                        stack.pop()
                    elif(i=='}' and stack[-1]=='{'):
                        stack.pop()
                    elif(i==']' and stack[-1]=='['):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack)==0