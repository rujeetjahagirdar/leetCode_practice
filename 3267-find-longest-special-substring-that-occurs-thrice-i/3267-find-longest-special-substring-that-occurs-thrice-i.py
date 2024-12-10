class Solution:
    def maximumLength(self, s: str) -> int:
        ans = float('-inf')

        def checkSpecial(substr):
            return (substr[0]*len(substr) ==substr)
        
        # for j in range(len(s)):
        #     for i in range(1, len(s)):
        #         subStr = s[j:j+i]
        #         # print(subStr)
        #         if(checkSpecial(subStr)):
        #             cnt = 1
        #             for k in range(j+1, len(s)):
        #                 if(s[k:k+len(subStr)]==subStr):
        #                     cnt+=1
                            
        #             # print(subStr, cnt)
        #             if(cnt>=3):
        #                 ans=max(ans, len(subStr))
        # print(ans)
        # if(ans==float('-inf')):
        #     return -1
        # else:
        #     return ans
        #############################
        # for length in range(1, len(s)):
        #     freq = defaultdict(lambda: 0)
        #     for i in range(len(s)-length+1):
        #         subStr = s[i:i+length]
        #         if(checkSpecial(subStr)==False):
        #             continue
        #         freq[subStr]+=1
            
        #         if(checkSpecial(subStr)==True):
        #             for i in freq:
        #                 if(freq[i]>=3):
        #                     ans = max(ans, len(subStr))
        #         # print(freq)
        # print(ans)
        # if(ans!=float("-inf")):
        #     return ans
        # else:
        #     return -1
###############################
        #using two pointers.
        #loop i throught entire string
        #loop j through i to len string
            #check if s[i]==s[j], this will insure the substring is special
            #if subtring is not special break the j loop, and start from next i
        all_count = defaultdict(int)  #{(c, len):cnt}
        for i in range(len(s)):
            length = 0
            for j in range(i, len(s)):
                if(s[i]==s[j]):
                    length+=1
                    all_count[(s[i], length)]+=1
                else:
                    break
        print(all_count)

        for i in all_count:
            if(all_count[i]>=3):
                ans = max(ans, i[1])
        print(ans)
        if(ans==float('-inf')):
            return -1
        else:
            return ans