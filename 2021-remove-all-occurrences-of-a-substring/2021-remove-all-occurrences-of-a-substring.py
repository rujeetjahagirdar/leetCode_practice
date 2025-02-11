class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

            if(len(stack)>=len(part) and stack[-len(part):]==list(part)):
                stack = stack[:-(len(part))]
            # print(stack)
        print(''.join(stack))
        return(''.join(stack))