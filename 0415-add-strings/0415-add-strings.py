class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #first make both strings equal length by concatanating 0 before
        #then traverse from right to left
            #add number + carry
            #update carry

        #if carry remains:
            #add it to end of ans
        #return reversed ans

        #TC: O(max of length of num1, num2)
        #SC: O((max of length of num1, num2) + 1)

        ans=''

        if(len(num1)<len(num2)):
            num1 = num1.rjust(len(num2), '0')
        if(len(num2)<len(num1)):
            num2 = num2.rjust(len(num1), '0')
        
        carry = 0

        for i in range(len(num1)-1, -1, -1):
            n = int(num1[i]) + int(num2[i]) + carry
            ans+=str(n%10)
            carry = n//10
        
        if(carry>0):
            ans+=str(carry)
        
        return ans[::-1]