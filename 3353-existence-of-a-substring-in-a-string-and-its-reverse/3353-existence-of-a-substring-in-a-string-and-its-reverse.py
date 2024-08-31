class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)-1):
            print(s[i+1]+s[i])
            if(s[i+1]+s[i] in s):
                return True
        return False