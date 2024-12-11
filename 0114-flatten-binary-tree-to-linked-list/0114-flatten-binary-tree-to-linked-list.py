# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return []
        nodeList = []

        def traverse(root):
            if not root:
                return
            nodeList.append(root)

            traverse(root.left)
            traverse(root.right)
            return
        
        traverse(root)
        print(nodeList)

        for i in range(len(nodeList)-1):
            nodeList[i].left = None
            nodeList[i].right = nodeList[i+1]
        nodeList[-1].left = None
        nodeList[-1].right = None
        root = nodeList[0]