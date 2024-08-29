class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def digitSum(s):
            print(s)
            ans=0
            for i in s:
                ans +=int(i)
            return str(ans)
        sTemp = s
        while(len(sTemp)>k):
            # print(''.join([digitSum(sTemp[i:i+k]) for i in range(0, len(sTemp), k)]))
            # break
            sTemp = ''.join([digitSum(sTemp[i:i+k]) for i in range(0, len(sTemp), k)])
        print(sTemp)
        return sTemp
        # for i in range(0, len(sTemp), k):
        #     print(sTemp[i:i+k])