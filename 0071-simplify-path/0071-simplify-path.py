class Solution:
    def simplifyPath(self, path: str) -> str:
        ans=[]

        folders = path.split('/')

        for f in folders:
            if(f==''):
                pass
            elif(f=='..'):
                if(ans):
                    ans.pop()
            elif(f=='.'):
                pass
            else:
                ans.append(f)
        
        print(ans)

        return "/"+"/".join(ans)