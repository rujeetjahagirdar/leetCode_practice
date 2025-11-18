class Solution:
    def maxOperations(self, s: str) -> int:
        number_of_ones=0
        ans=0

        for i in range(len(s)):
            if(s[i]=='1'):
                number_of_ones+=1
            else:
                if(i>0 and s[i-1]=='1'): #found '10'
                    ans+=number_of_ones
        
        return ans