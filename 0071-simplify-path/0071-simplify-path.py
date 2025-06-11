class Solution:
    def simplifyPath(self, path: str) -> str:
        ans='/'
        stack=[]
        # print(path)
        pathList =path.split('/') 
        # print("pathList= ",pathList)
        for i in pathList:
            # print(i)
            if(i=='.' or i==''):
                pass
            elif(i=='..'):
                if(len(stack)>0):
                    stack.pop()
            else:
                stack.append(i)
            # print(stack)
        return(ans+'/'.join(stack))
             