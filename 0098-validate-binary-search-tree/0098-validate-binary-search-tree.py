# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_value = float('inf')
        min_value = float('-inf')

        #DFS
        stack = [(root, min_value, max_value)]

        while stack:
            n, min_value, max_value = stack.pop()

            if not(min_value<n.val<max_value):
                return False
            
            if(n.right):
                stack.append((n.right, n.val, max_value))
            
            if(n.left):
                stack.append((n.left, min_value, n.val))
        
        return True