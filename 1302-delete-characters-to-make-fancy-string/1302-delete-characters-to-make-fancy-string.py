class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        # cnt=1

        for i in range(len(s)):
            if(len(stack)>=2 and (stack[-2]==stack[-1]==s[i])):
                continue
            stack.append(s[i])
        print(stack)

        return ''.join(stack)