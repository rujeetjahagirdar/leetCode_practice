class Solution:
    def myAtoi(self, s: str) -> int:
        sign = []
        number = []
        s=s.strip()
        for i in range(len(s)):
            if(s[i]==" "):
                break
            elif(s[i]=="-" or s[i]=="+"):
                if(i==0 or s[i-1]==' '):
                    sign.append(s[i])
                else:
                    break
            elif(s[i].isnumeric()):
                number.append(s[i])
            else:
                break
        print(sign)
        print(number)
        ans=''
        if(len(number)!=0):
            for i in range(len(number)):
                if(len(number)==1 and number[i]=='0'):
                    ans =0
                else:
                    ans +=number[i]
        else:
            return 0
        if(len(sign)!=0):
            if(sign[0]=='-'):
                ans = -1 * int(ans)
            else:
                ans = int(ans)
        print(int(ans))
        return max(-2**31, min(int(ans), 2**31 - 1))