class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = Counter(s)
        ans=''

        for i in order:
            if(i in c):
                ans+=i*c[i]

                del c[i]
        
        if(len(c)>0):
            for i in c:
                ans+=i*c[i]
        
        return(ans)