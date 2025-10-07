class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices_to_remove = []

        for i in range(len(s)):
            if(s[i]=='('):
                indices_to_remove.append(i)
            elif(s[i]==')'):
                if(len(indices_to_remove)>0 and s[indices_to_remove[-1]]=='('):
                    indices_to_remove.pop()
                else:
                    indices_to_remove.append(i)
        print(indices_to_remove)

        ans=''
        for i in range(len(s)):
            if(i not in indices_to_remove):
                ans+=s[i]
        
        print(ans)
        return ans