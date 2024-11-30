class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=[]
        n = max(len(a), len(b))

        a=a.rjust(n, '0')
        b=b.rjust(n, '0')

        print(a)
        print(b)

        carry='0'

        for i in range(n-1, -1, -1):
            n1=a[i]
            n2=b[i]
            # print(n1)
            # print(n2)

            if(n1=='1' and n2=='1'):
                if(carry=='1'):
                    ans.append('1')
                    carry='1'
                else:
                    ans.append('0')
                    carry='1'
            elif(n1=='0' and n2=='0'):
                if(carry=='1'):
                    ans.append('1')
                    carry='0'
                else:
                    ans.append('0')
                    carry='0'
            else:
                if(carry=='1'):
                    ans.append('0')
                    carry='1'
                else:
                    ans.append('1')
                    carry='0'
        if(carry=='1'):
            ans.append('1')
        print(ans)
        return ''.join(ans[::-1])