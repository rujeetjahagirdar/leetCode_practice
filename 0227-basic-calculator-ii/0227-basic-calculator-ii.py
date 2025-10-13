class Solution:
    def calculate(self, s: str) -> int:
        #there will be a number between two operations
        # +32-
        # *12/
        #so when you come across an operation, we check if number in between is greater than zero, check last 
        # operation, if number is zero (first char is an operation) update last operation, if number is not zero, if last operatino is + or -, append number with this last operation sign and append to list, if last operation is * or /, pop last number from stack and perform last operation's operation with current number and poped number and append result to stack, update last operation to current operation symbol

        #at last sum the stack values and return as result

        stack = []
        last_operation = "+"
        n = 0
        #-3*4
        #0*1
        for i in range(len(s)):
            if(s[i].isdigit()):
                n = n*10 + int(s[i])
            if(i ==len(s)-1 or s[i] in '+-*/'):
                # if(n==0):
                #     last_operation = s[i]
                # else:
                if(last_operation=="+"):
                    stack.append(n)
                    n = 0
                elif(last_operation=='-'):
                    stack.append(-n)
                    n=0
                elif(last_operation=='*'):
                    first_num = stack.pop()
                    stack.append(first_num*n)
                    n=0
                elif(last_operation=='/'):
                    first_num = stack.pop()
                    stack.append(int(first_num/n))
                    n=0
                    
                last_operation = s[i]
                # print(stack)
        return sum(stack)