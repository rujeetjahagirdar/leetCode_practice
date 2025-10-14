class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        paths = path.split("/")
        #/home//foo/
        #['', home, '',foo]

        for p in paths:
            if(p==".."):
                if(len(stack)>0):
                    stack.pop()
            elif(p=='' or p=='.'):
                continue
            else:
                stack.append(p)
        print(stack)

        return '/'+'/'.join(stack)
        