class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.lstrip().rstrip()
        stack = s.split(" ")
        print(stack)

        ans=[]

        while stack:
            word = stack.pop()
            if(word!=''):
                ans.append(word)
        
        print(ans)
        print(' '.join(ans))
        return ' '.join(ans)