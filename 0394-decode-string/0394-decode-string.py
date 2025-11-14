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

        stack = []

        i=0
        n=0
        while(i<len(s)):

            #check digit
            if(s[i].isnumeric()):
                # while(s[i].isnumeric()):
                n = n*10+int(s[i])
                    # i+=1
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
                    tempStr = tempStr[::-1] #reverse the string
                    stack.pop() #ignore opening bracket
                    freq = stack.pop() #get freq
                    tempStr = tempStr*freq

                    for c in tempStr:
                        stack.append(c)
            
            # print(stack)
            i+=1
        print(stack)
        return ''.join(stack)
                    

            
