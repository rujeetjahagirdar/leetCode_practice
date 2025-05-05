class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        sm = x
        crry = y

        while(crry):
            sm, crry = sm ^ crry, (sm&crry)<<1
        
        return(bin(sm)[2:])