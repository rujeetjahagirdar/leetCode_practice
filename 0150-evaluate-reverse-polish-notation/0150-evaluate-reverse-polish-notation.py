class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if(len(tokens)==1):
        #     return int(tokens[0])
        
        # stack=[]

        # for i in range(len(tokens)):
        #     if(tokens[i][0]=='-' and tokens[i][1:].isdigit()):
        #         stack.append(int(tokens[i]))
        #     elif(tokens[i].isdigit()):
        #         stack.append(int(tokens[i]))
        #     else:
        #         num2 = stack.pop(-1)
        #         num1 = stack.pop(-1)
        #         if(tokens[i]=='+'):
        #             result = num1 + num2
        #         elif(tokens[i]=='-'):
        #             result = num1 - num2
        #         elif(tokens[i]=='*'):
        #             result = num1 * num2
        #         elif(tokens[i]=='/'):
        #             result = int(num1 / num2)
        #         stack.append(result)
        #     # print(stack)
        
        # # print(result)
        # return stack[0]

        if(len(tokens)==1):
            return int(tokens[0])
        
        stack=[]

        for token in tokens:
            if(token.isdigit() or (token[0]=='-' and token[1:].isdigit())):
                stack.append(int(token))
            else:
                if(len(stack)<2):
                    return False
                else:
                    op = token
                    num2 = stack.pop(-1)
                    num1 = stack.pop(-1)

                    if(op=='+'):
                        stack.append(num1+num2)
                    elif(op=='-'):
                        stack.append(num1-num2)
                    elif(op=='/'):
                        stack.append(int(num1/num2))
                    elif(op=='*'):
                        stack.append(num1*num2)
            # print(stack)
        
        return stack[0]
