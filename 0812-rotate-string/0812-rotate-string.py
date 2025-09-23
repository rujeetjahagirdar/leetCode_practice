class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(len(s)!=len(goal)):
            return False

        t=s
        for _ in range(10):
            t+=t
        print(goal)
        
        print(goal in t)
        
        if(goal in t):
            return True
        return False
