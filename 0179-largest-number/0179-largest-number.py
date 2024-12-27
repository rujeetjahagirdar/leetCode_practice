class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # listOfDigits = []

        # for n in nums:
        #     if(n>9):
        #         t = []
        #         while(n>9):
        #             t.append(n%10)
        #             n=n//10
        #         t.append(n)
        #         listOfDigits.extend(t)
        #     else:
        #         listOfDigits.append(n)
        
        # listOfDigits = sorted(listOfDigits, reverse=True)
        # print(listOfDigits)
        # # print(''.join(listOfDigits))
        # return ''.join([str(i) for i in listOfDigits])

        #################
        lenOfMaxNum = len(str(max(nums)))

        numsStr = [str(n) for n in nums]

        # numsStr.sort(key=lambda x:x*(lenOfMaxNum-len(x) +1), reverse=True)
        numsStr.sort(key=lambda x:x*(lenOfMaxNum), reverse=True)

        if(numsStr[0]=='0'):
            return '0'

        print(numsStr)
        return ''.join(numsStr)