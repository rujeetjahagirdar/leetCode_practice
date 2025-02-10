class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if(s[i].isalpha()):
                stack.append(s[i])
            else:
                if(len(stack)>0):
                    stack.pop(-1)
        print(stack)
        return("".join(stack))