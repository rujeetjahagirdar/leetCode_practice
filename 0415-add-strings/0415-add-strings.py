class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if(len(num1)<len(num2)):
            num1=num1.rjust(len(num2), '0')
        elif(len(num1)>len(num2)):
            num2=num2.rjust(len(num1), '0')
        

        ans=''
        carry=0

        for i in reversed(range(len(num1))):
            sm = int(num1[i])+int(num2[i])+carry
            carry=0
            if(sm>=10):
                carry = 1
                ans+=str(sm%10)
                # carry=0
            else:
                ans+=str(sm%10)
            # print(ans)
        if(carry==1):
            return '1'+ans[::-1]
        return ans[::-1]
            
