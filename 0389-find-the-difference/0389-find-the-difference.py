class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sXor = 0
        tXor = 0

        for i in s:
            sXor = sXor ^ ord(i)
        
        for i in t:
            tXor = tXor ^ ord(i)

        return chr(sXor ^ tXor)