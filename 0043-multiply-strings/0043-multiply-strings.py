class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapping = {str(i): i for i in range(10)}
        # print(mapping)
        # n1 = len(num1)
        # n2 = len(num2)
        # if(n1>=n2):
        #     num2.rjust(n1, '0')
        # else:
        #     num2.rjust(n1, '0')
        ans=[]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            tAns = [0]*i
            carry = 0
            for j in range(len(num1)):
                mult = mapping[num1[j]] * mapping[num2[i]]
                tAns.append((mult)%10 + carry)
                carry = mult //10
            if(carry!=0):
                tAns.append(carry)
            ans.append(tAns[::-1])
            
        print(ans)
        finalAns = 0
        for i in range(len(ans)):
            t = 0
            for j in range(len(ans[i])):
                # print(ans[i][j])
                # print(ans[i][j]*pow(10,len(ans[i])-j-1), pow(10,len(ans[i])-j-1))
                t += ans[i][j]*pow(10,len(ans[i])-j-1)
                # print(t)
            # print(t)
            finalAns +=t
            # break
        return str(finalAns)