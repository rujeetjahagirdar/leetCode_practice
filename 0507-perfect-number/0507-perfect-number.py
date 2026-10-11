class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans=0

        for i in range(1, int(num**0.5) +1):
            if(num%i==0):
                ans+=i

                if(i*i !=num):
                    ans+=num//i
        
        return (ans - num)==num