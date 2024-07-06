class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        stack = []
        for i in s:
            if(i in vowels):
                stack.append(i)
        ans=''
        for i in s:
            if(i in vowels):
                ans = ans + stack.pop()
            else:
                ans = ans + i
        return(ans)