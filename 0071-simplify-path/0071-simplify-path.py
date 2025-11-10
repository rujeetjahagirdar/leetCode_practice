class Solution:
    def simplifyPath(self, path: str) -> str:
        
        folders = path.split('/')

        ans = []

        for f in folders:
            if(f=='.' or f=='/' or f==''):
                pass
            elif(f=='..'):
                if(ans):
                    ans.pop()
            else:
                ans.append(f)
        
        print(ans)

        return '/'+'/'.join(ans)