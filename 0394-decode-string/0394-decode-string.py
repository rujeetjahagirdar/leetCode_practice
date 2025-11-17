class Solution:
    def decodeString(self, s: str) -> str:

        #if opening bracket, put aside curret number and current string

        # numStack = []
        # strStack = []
        # tStr = ''
        # num = 0

        # for i in s:
        #     if(i.isnumeric()):
        #         num = num*10+int(i)
        #     elif(i=='['):
        #         # if(tStr):
        #         strStack.append(tStr)
        #         tStr = ''
        #         # if(num>0):
        #         numStack.append(num)
        #         num=0
        #     elif(i==']'):
        #         freq = numStack.pop()
        #         if(strStack):
        #             tStr = strStack.pop() + freq*tStr
        #         else:
        #             tStr = freq*tStr
        #     else:
        #         tStr+=i
        #     # print(tStr)
        # return tStr

        #############################

        #approach 2: using one stack
        #parse the string, push number, opening bracket and chars on stack, when closing bracket occurs, pop from stack until opening bracket, then decode string by frequency and again push this string(from left to right) on stack and continue this process
        #in the end, answer will be the stack
        #NOTE: when opening bracket occurs, push the current number on the stack and make number 0

        stack = []

        i=0
        n=0
        while(i<len(s)):

            #check digit
            if(s[i].isnumeric()):
                n = n*10+int(s[i])
            else:
                if(s[i]=='['):
                    stack.append(n)
                    n=0

                if(s[i]=='[' or s[i].isalpha()):
                    stack.append(s[i])
                else:
                    tempStr=''
                    while(stack[-1]!='['):
                        tempStr+=stack.pop()
                        # tempStr+=stack.pop()[::-1], method 2
                    tempStr = tempStr[::-1] #reverse the string
                    stack.pop() #ignore opening bracket
                    freq = stack.pop() #get freq
                    tempStr = tempStr*freq

                    for c in tempStr:
                        stack.append(c)
                    # stack.append(tempStr) , method 2
            print(stack)
                    
            
            # print(stack)
            i+=1
        print(stack)
        return ''.join(stack)
                    

            
