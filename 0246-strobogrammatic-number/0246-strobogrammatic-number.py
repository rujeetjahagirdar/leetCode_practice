class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        mapping = {'6':'9', '9':'6', '8':'8', '1':'1', '0':'0'}

        l=0
        r=len(num)-1

        while(l<=r):
            if(num[l] not in mapping or num[r] not in mapping):
                return False
            if(num[l]!=mapping[num[r]]):
                return False
            l+=1
            r-=1
        return True