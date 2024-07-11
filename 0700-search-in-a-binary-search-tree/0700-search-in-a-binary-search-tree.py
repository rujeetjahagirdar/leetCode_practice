# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # print(root)
        if not root:
            # print(ro Noneot.val)
            return None
        if root.val == val:
            # print("Foudn ",root.val)
            return root
        elif root.val > val:
            # print("In left: ",root.val)
            return self.searchBST(root.left, val)
        elif root.val < val:
            # print(root.val)
            return self.searchBST(root.right, val)
    # searchBST(root,val)