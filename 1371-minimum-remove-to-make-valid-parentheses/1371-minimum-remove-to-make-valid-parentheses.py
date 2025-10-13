class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        removeIndex = []

        #if opening add to stack
        #if closing, if stack -1 is opening, pop stack
                    # else add to stack
        #make new string by removeing stack index

        for i in range(len(s)):
            if(s[i]=='('):
                removeIndex.append(i)
            elif(s[i]==')'):
                if(removeIndex and s[removeIndex[-1]]=='('):
                    removeIndex.pop()
                else:
                    removeIndex.append(i)
        ans=''

        for i in range(len(s)):
            if(i not in removeIndex):
                ans+=s[i]
        
        return ans