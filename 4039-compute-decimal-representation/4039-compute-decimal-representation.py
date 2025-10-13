class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        
        i=0
        ans=[]
        #21
        while(n>0):
            if(n%10==0):
                n=n//10
                i+=1
                continue
            ans.append(n%10 * 10**i)
            i+=1
            n=n//10
        return ans[::-1]