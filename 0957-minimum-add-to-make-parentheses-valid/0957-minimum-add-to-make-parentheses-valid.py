class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        stack=[]
        closing_count=0
        for i in s:
            if(len(stack)==0):
                stack.append(i)
            else:
                if(i=='('):
                    stack.append(i)
                elif(i==")" and stack[-1]=="("):
                    stack.pop()
                elif(i==")"):
                    closing_count+=1
        return len(stack)+closing_count