class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if(len(s)%2!=0):
        #     for i in range(1, len(s),2):
        #         subStr = s[:i]
        #         repetations = len(s)//len(subStr)
        #         if(subStr*repetations ==s):
        #             return True
        # else:
        #     for i in range(1,len(s)):
        #         subStr = s[:i]
        #         repetations = len(s)//len(subStr)
        #         # print(subStr, repetations)
        #         if(subStr*repetations ==s):
        #             return True
        # return False

        n = len(s)

        for i in range(1, n//2 +1):
            if(n % i==0):  #if evenly divided by subStr length
                subStr = s[:i]
                repetations = n//i

                if(subStr*repetations==s):
                    return True
        return False