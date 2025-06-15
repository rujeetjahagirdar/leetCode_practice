class Solution:
    def maxDiff(self, num: int) -> int:
        strNum = str(num)
        maxNum = ''
        minNum = ''

        i=0
        maxNum = strNum[:]
        while(i<len(strNum) and strNum[i]=='9'):
            i+=1
        if(i<len(strNum)):
            maxNum = strNum.replace(strNum[i], '9')

        if(strNum[0]=='1'):
            i=1
            while(i<len(strNum) and (strNum[i]=='1' or strNum[i]=='0')):
                i+=1
            if(i<len(strNum)):
                minNum = strNum.replace(strNum[i], '0')
            else:
                minNum = strNum[:]
        else:
            minNum = strNum.replace(strNum[0], '1')
        
        print(maxNum)
        print(minNum)
        return (int(maxNum)-int(minNum))