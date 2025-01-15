class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        strbinNum1 = str(bin(num1))[2:]
        strbinNum2 = str(bin(num2))[2:]
        n = max(len(strbinNum1), len(strbinNum2))
        strbinNum1 = strbinNum1.rjust(n, '0')
        strbinNum2 = strbinNum2.rjust(n, '0')

        print(strbinNum1)
        print(strbinNum2)

        n1Count = strbinNum1.count('1')
        n2Count = strbinNum2.count('1')

        ans=list(strbinNum1)

        if(n1Count==n2Count):
            return num1
        elif(n1Count>n2Count):
            diff = n1Count-n2Count
            for i in range(len(strbinNum1))[::-1]:
                if(strbinNum1[i]=='1' and diff>0):
                    ans[i]='0'
                    diff-=1
                    if(diff==0):
                        break
        else:
            diff = n2Count-n1Count
            for i in range(len(strbinNum1))[::-1]:
                if(strbinNum1[i]=='0' and diff>0):
                    ans[i]='1'
                    diff-=1
                    if(diff==0):
                        break
        print(ans)
        return int(''.join(ans),2)