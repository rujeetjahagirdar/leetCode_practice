# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSmallest(self, root):
        if not root.left:
            return root
        return self.findSmallest(root.left)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        else:
            # Checks for Lesser value
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            # Checks for Greater value
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            # Checks if we have reached the node we want to delete
            else:
                # First we check if only 1 child node is present
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    temp = self.findSmallest(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
            return root