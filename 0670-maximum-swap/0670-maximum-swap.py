class Solution:
    def maximumSwap(self, num: int) -> int:
        strNum = list(str(num))

        mxTill = [-1]*len(strNum)
        mx = (strNum[-1], len(strNum)-1)
        mxTill[-1]=mx
        
        for i in range(len(strNum)-2, -1, -1):
            if(int(strNum[i])>int(mx[0])):
                mxTill[i] = (int(strNum[i]), i)
                mx = (int(strNum[i]), i)
            else:
                mxTill[i]= mx
        
        print(mxTill)

        ans=''

        for i in range(len(strNum)):
            if(int(mxTill[i][0])>int(strNum[i])):
                strNum[i], strNum[mxTill[i][1]] = str(mxTill[i][0]), strNum[i]
                print(strNum)
                return int(''.join(strNum))
        return int(''.join(strNum))