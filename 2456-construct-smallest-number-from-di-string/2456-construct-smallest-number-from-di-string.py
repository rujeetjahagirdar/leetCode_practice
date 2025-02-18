class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans=''
        stack=[]
        mx=float("-inf")
        for i in range(len(pattern)):
            if(pattern[i]=='I'):
                mx = max(i+1, mx)
                ans+=str(i+1)
                if(len(stack)>0):
                    while(stack):
                        ans+=str(stack.pop(-1))
                print(ans)
            else:
                stack.append(i+1)
                print("stack= ", stack)
        
        
        if(pattern[-1]=='D' and stack):
            stack.append(i+2)
            while(stack):
                ans+=str(stack.pop(-1))
        if(pattern[-1]=='I'):
            ans+=str(mx+1)
        print(ans)
        return ans

# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
#         ans=''
#         stack = []

#         for i in range(len(pattern)+1):
#             stack.append(str(i+1))

#             if(i==len(pattern) or pattern[i]=='I'):
#                 while(stack):
#                     ans+=stack.pop(-1)
        
#         print(ans)
#         return ans