class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'1':'1', '6':'9', '8':'8', '0':'0', '9':'6'}

        l=0
        r=len(num)-1

        while(l<=r):
            if(num[l] not in mapping or mapping[num[l]]!=num[r]):
                return False
            l+=1
            r-=1

        return True