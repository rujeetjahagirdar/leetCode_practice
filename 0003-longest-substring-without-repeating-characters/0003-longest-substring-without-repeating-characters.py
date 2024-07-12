class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        maxLength=0
        for i in range(len(s)-1):
            substr=s[i]
            tempLength=1
            for j in range(i+1,len(s)):
                if(s[j] not in substr):
                    substr = substr + s[j]
                    tempLength = tempLength + 1
                    # print(substr, tempLength)
                else:
                    # print("in else")
                    # print(substr, tempLength)
                    if(tempLength>maxLength):
                        maxLength = tempLength
                    break
            if(tempLength>maxLength):
                        maxLength = tempLength
        # print(maxLength)
        return maxLength