class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if(i in ')]}'):
                if(not stack):
                    return False
                else:
                    if(stack[-1]!=mapping[i]):
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(i)
        if(len(stack)==0):
            return True
        return False