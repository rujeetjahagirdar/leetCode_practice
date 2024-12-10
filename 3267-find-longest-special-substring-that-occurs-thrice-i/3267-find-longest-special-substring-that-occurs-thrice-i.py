class Solution:
    def maximumLength(self, s: str) -> int:
        ans = float('-inf')

        def checkSpecial(substr):
            return (substr[0]*len(substr) ==substr)
        
        for j in range(len(s)):
            for i in range(1, len(s)):
                subStr = s[j:j+i]
                # print(subStr)
                if(checkSpecial(subStr)):
                    cnt = 1
                    for k in range(j+1, len(s)):
                        if(s[k:k+len(subStr)]==subStr):
                            cnt+=1
                            
                    # print(subStr, cnt)
                    if(cnt>=3):
                        ans=max(ans, len(subStr))
        print(ans)
        if(ans==float('-inf')):
            return -1
        else:
            return ans