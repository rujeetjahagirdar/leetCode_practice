# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]

        if not root:
            return ''
        
        def dfs(root, tNum):

            if not root:
                return ''
            
            tNum +=str(root.val)

            if(not root.left and not root.right):
                ans.append(tNum)
                print(ans)
        
            dfs(root.left, tNum)
            dfs(root.right, tNum)
            return 


        dfs(root, '')

        a = 0
        for i in ans:
            a+=int(i)
        return a