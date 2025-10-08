class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path = path.split("/")

        for i in path:
            if(i=='.' or i==''):
                continue
            elif(i==".."):
                if(ans):
                    ans.pop()
            else:
                ans.append(i)
        print(ans)
        return '/'+'/'.join(ans)
        
        