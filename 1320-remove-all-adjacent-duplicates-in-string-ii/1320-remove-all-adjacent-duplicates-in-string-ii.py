class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #(c, count)

        for i in range(len(s)):
            if(i==0 or len(stack)==0):
                stack.append((s[i], 1))
            else:
                # print(s[i], stack[-1][1])
                if(s[i]==stack[-1][0]):
                    c, cnt = stack.pop()
                    stack.append((c, cnt+1))

                    if(stack[-1][1]==k):
                        stack.pop()
                else:
                    stack.append((s[i], 1))
            # print(stack)
        
        return ''.join(i[0]*i[1] for i in stack)