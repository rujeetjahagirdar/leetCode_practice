class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        removeIndex = []

        for i in range(len(s)):
            if(s[i]=='('):
                removeIndex.append(i)
            elif(s[i]==')'):
                if(len(removeIndex)==0):
                    removeIndex.append(i)
                else:
                    if(s[removeIndex[-1]]=='('):
                        removeIndex.pop()
                    else:
                        removeIndex.append(i)
        # print(removeIndex)
        removeIndexSet = set(removeIndex)
        ans = ''
        for i in range(len(s)):
            if(i not in removeIndexSet):
                ans+=s[i]
        
        return ans