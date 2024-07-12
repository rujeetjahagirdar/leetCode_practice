class Solution:
    def checkEqual(self, s1, s2):
        if(sorted(list(s1))==sorted(list(s2))):
            return True
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range((len(s2)-len(s1))+1):
            substr = s2[i:i+len(s1)]
            if(self.checkEqual(s1, substr)):
                return True
        return False