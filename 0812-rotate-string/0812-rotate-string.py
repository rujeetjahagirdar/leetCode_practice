class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(len(s)!=len(goal)):
            return False

        t=s
        for _ in range(2):
            t+=t
        
        if(goal in t):
            return True
        return False
