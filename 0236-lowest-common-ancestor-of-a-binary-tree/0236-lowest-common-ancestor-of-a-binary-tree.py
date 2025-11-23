# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #dfs, bottom up
        #process current node after processing children

        #TC: O(n)
        #SC: O(n)

        def dfs(node):
            if not node:
                return None
            
            if(node==p or node==q):
                return node
            
            left_found = dfs(node.left)
            right_found = dfs(node.right)

            if(left_found and right_found):
                return node

            return left_found or right_found
        
        return(dfs(root))