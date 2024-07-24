# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and not t2:
                return False
            if not t1 and t2:
                return False
            if(t1.val==t2.val):
                return (sameTree(t1.left, t2.left) and
                sameTree(t1.right, t2.right))
            else:
                return False
        
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if(sameTree(root, subRoot)):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
            