class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        max_len = min(len1, len2)
    
        for i in range(max_len, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                divisor = str1[:i]
                if str1 == divisor * (len1 // i) and str2 == divisor * (len2 // i):
                    return divisor
        return ""