class Solution:
    def reverseVowels(self, s: str) -> str:
        stack=[]

        for i in s:
            if(i in 'aeiouAEIOU'):
                stack.append(i)
        
        ans=''

        for i in s:
            if(i in 'aeiouAEIOU'):
                ans+=stack.pop()
            else:
                ans+=i
        
        print(ans)
        return ans