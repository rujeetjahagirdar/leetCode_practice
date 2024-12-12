# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        unique_values = set()

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            unique_values.add(node.val)
            inorder(node.right)  
        

        inorder(root)
        print(unique_values)
        unique_values.remove(root.val)
        if unique_values:
            return min(unique_values)
        else:
            return -1