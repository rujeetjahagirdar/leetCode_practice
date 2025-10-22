class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        
        revNum=0

        n = x

        while(x>0):
            revNum = revNum*10 + x%10
            x = x//10
        
        print(n)
        print(revNum)

        return n==revNum

