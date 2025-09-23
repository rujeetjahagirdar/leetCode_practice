class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        l=0
        r = len(num)-1

        strobogrammatic_pairs = {'6':'9', '9':'6', '0':'0', '8':'8', '1':'1'}

        while(l<=r):
            if(num[l] not in strobogrammatic_pairs or num[r] not in strobogrammatic_pairs):
                return False
            if(strobogrammatic_pairs[num[l]]!=num[r]):
                return False
            l+=1
            r-=1
        return True
