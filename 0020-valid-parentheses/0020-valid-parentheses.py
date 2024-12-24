class Solution:
    def isValid(self, s: str) -> bool:
        # hashM = {'(':0, '{':0, '[':0}
        # for i in s:
        #     if(i=='('):
        #         hashM[i] = hashM[i]+1
        #     elif(i=='{'):
        #         hashM[i] = hashM[i]+1
        #     elif(i=='['):
        #         hashM[i] = hashM[i]+1
        #     elif(i==')'):
        #         if(hashM['(']==0):
        #             return False
        #         hashM['('] = hashM['(']-1
        #     elif(i==']'):
        #         if(hashM['[']==0):
        #             return False
        #         hashM['['] = hashM['[']-1
        #     elif(i=='}'):
        #         if(hashM['{']==0):
        #             return False
        #         hashM['{'] = hashM['{']-1
        # for n in list(hashM.values()):
        #     if(n!=0):
        #         return False
        # return True

        #stack
        stack=[]
        parentheses_pairs = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if(i in parentheses_pairs):
                if(stack and stack[-1]==parentheses_pairs[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if(stack):
            return False
        else:
            return True