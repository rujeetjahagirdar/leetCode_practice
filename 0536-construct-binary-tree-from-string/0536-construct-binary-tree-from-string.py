# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:

#     def process_string(self, s):
#         s = list(s)
#         ans=[]
#         #['-', '4', '(', '2', '(', '3', ')', '(', '1', ')', ')', '(', '6', '(', '5', ')', '(', '7', ')', ')']
#         #['5', '1', '(', '2', '3', '2', ')', '(', '4', '3', '4', ')']

#         i=0
#         is_negative = False
#         for j in range(i,len(s)):
#             if(s[j].isnumeric()):
#                 continue
#             # elif(s[j]=='-'):
#             #     is_negative=True
#             elif(s[j]=='(' or s[j]==')'):
#                 num = ''.join(s[i:j])
#                 # print(''.join(s[i:j]))
#                 # if(is_negative):
#                 #     num *=-1
#                 #     is_negative=False
#                 if(num==''):
#                     continue
#                 ans.append(num)
#                 ans.append(s[j])
#                 i=j
#                 while(i<len(s) and not s[i].isnumeric()):
#                     ans.append(s[i])
#                     i+=1
                
#         print(ans)
#         return ans

        

#     def str2tree(self, s: str) -> Optional[TreeNode]:

#         if(not s):
#             return

#         s = self.process_string(s)
#         stack=[]

#         is_negative = False
#         open_count=0
#         for i in range(len(s)):
#             if(s[i][0]=='-'):
#                 is_negative=True
#                 continue
#             if(s[i].isnumeric()):
#                 if(is_negative):
#                     stack.append(TreeNode(-int(s[i])))
#                     is_negative=False
#                 else:
#                     stack.append(TreeNode(int(s[i])))
#             elif(s[i]=="("):
#                 open_count+=1
#             else:
#                 # if(open_count==1):
#                 #     n=stack.pop()
#                 #     continue

#                 n = stack.pop()
#                 if(stack[-1].left ==None):
#                     stack[-1].left = n
#                 elif(stack[-1].right==None):
#                     stack[-1].right = n
                
#                 open_count-=1
#             print(stack)
#                 # if(open_count==0):
#         return stack[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        i = 0
        n = len(s)
        stack = []

        while i < n:
            ch = s[i]
            if ch == ')':
                # finished a child, attach to parent
                child = stack.pop()
                if stack:
                    parent = stack[-1]
                    if parent.left is None:
                        parent.left = child
                    else:
                        parent.right = child
                i += 1
            elif ch == '(':
                i += 1
            else:
                # parse number (with optional '-')
                sign = 1
                if s[i] == '-':
                    sign = -1
                    i += 1
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + (ord(s[i]) - 48)
                    i += 1
                node = TreeNode(sign * num)
                stack.append(node)

        return stack[0] if stack else None
