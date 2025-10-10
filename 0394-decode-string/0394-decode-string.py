class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        tStr = ''
        num = 0

        for i in s:
            if(i.isnumeric()):
                num = num*10+int(i)
            elif(i=='['):
                # if(tStr):
                strStack.append(tStr)
                tStr = ''
                # if(num>0):
                numStack.append(num)
                num=0
            elif(i==']'):
                freq = numStack.pop()
                if(strStack):
                    tStr = strStack.pop() + freq*tStr
                else:
                    tStr = freq*tStr
            else:
                tStr+=i
            # print(tStr)
        return tStr

                