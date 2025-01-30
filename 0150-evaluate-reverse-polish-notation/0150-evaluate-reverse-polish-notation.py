class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if(len(tokens)==1):
            return int(tokens[0])
        
        stack=[]

        for i in range(len(tokens)):
            if(tokens[i][0]=='-' and tokens[i][1:].isdigit()):
                stack.append(int(tokens[i]))
            elif(tokens[i].isdigit()):
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                if(tokens[i]=='+'):
                    result = num1 + num2
                elif(tokens[i]=='-'):
                    result = num1 - num2
                elif(tokens[i]=='*'):
                    result = num1 * num2
                elif(tokens[i]=='/'):
                    result = int(num1 / num2)
                stack.append(result)
            # print(stack)
        
        # print(result)
        return stack[0]