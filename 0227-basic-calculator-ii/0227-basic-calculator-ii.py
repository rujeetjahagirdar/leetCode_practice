class Solution:
    def calculate(self, s: str) -> int:
        
        ans = []
        currentNum=0
        lastOperation="+"

        for i in range(len(s)):
            if(s[i].isnumeric()):
                currentNum = currentNum*10+int(s[i])
            if(s[i] in ('+-*/') or i==len(s)-1):
                if(lastOperation=='+'):
                    ans.append(currentNum)
                    currentNum = 0
                    lastOperation = s[i]
                elif(lastOperation=='-'):
                    ans.append(-currentNum)
                    currentNum=0
                    lastOperation = s[i]
                elif(lastOperation=='*'):
                    n1 = ans.pop()
                    ans.append(n1*currentNum)
                    currentNum=0
                    lastOperation=s[i]
                elif(lastOperation=='/'):
                    n1 = ans.pop()
                    ans.append(int(n1/currentNum))
                    currentNum=0
                    lastOperation=s[i]
            # print(ans)
        return sum(ans)