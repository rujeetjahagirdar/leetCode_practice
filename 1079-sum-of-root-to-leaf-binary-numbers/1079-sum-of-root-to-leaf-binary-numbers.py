# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        #dfs
        #if its leaf, then convert current binary number to base 2 and add to sum

        ans=0

        def dfs(node, n):

            nonlocal ans

            if(not node):
                return
            
            n= n*10 + node.val

            if(not node.left and not node.right):
                print(n)
                ans+=int(str(n), 2)
            if(node.left):
                dfs(node.left, n)
            
            if(node.right):
                dfs(node.right, n)
        
        dfs(root, 0)
        # print(ans)
        return ans