class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        c = Counter(ages)

        ans=0

        for agex in c:
            for agey in c:
                if(agey<= 0.5 * agex +7):
                    continue
                if(agey> agex):
                    continue
                if(agey>100 and agex<100):
                    continue
                
                ans +=c[agex]*c[agey]

                if(agex==agey):
                    ans-=c[agex]
        
        return(ans)